document.addEventListener("DOMContentLoaded", () => {
  let topicData = [];
  let currentActiveId = null;

  const topicListContainer = document.getElementById("topic-list");
  const transcriptBodyContainer = document.getElementById("transcript-body");
  const searchInput = document.getElementById("search-input");
  const totalTopicsCount = document.getElementById("total-topics-count");

  // Load JSON Topic Index Data with resilient fallback
  function loadTopicIndex() {
    const tryPaths = ["./topic_index.json", "../output/topic_index.json", "/output/topic_index.json"];
    
    function tryFetch(index) {
      if (index >= tryPaths.length) {
        console.warn("Using embedded fallback topic data");
        topicData = getFallbackTopicData();
        totalTopicsCount.textContent = `${topicData.length} Topics Identified`;
        renderTopicCards(topicData);
        fetchTranscriptText();
        return;
      }
      
      fetch(tryPaths[index])
        .then(res => {
          if (!res.ok) throw new Error("HTTP error " + res.status);
          return res.json();
        })
        .then(data => {
          topicData = data;
          totalTopicsCount.textContent = `${data.length} Topics Identified`;
          renderTopicCards(topicData);
          fetchTranscriptText();
        })
        .catch(() => tryFetch(index + 1));
    }
    
    tryFetch(0);
  }

  loadTopicIndex();

  function renderTopicCards(topics) {
    topicListContainer.innerHTML = "";
    topics.forEach((t, idx) => {
      const card = document.createElement("div");
      card.className = "topic-card";
      card.dataset.id = t.id;
      
      const catClass = `tag-${(t.topic_category || 'procedure').toLowerCase()}`;
      
      card.innerHTML = `
        <div class="card-top">
          <span class="topic-title">${t.topic}</span>
          <span class="location-badge">P${t.start_page}:${t.start_line} - P${t.end_page}:${t.end_line}</span>
        </div>
        <div class="card-tags">
          <span class="tag ${catClass}">${t.topic_category || 'General'}</span>
          ${t.is_reentry ? '<span class="tag tag-reentry">Re-entry 🔄</span>' : ''}
          ${t.is_digression ? '<span class="tag tag-digression">Digression ⏸️</span>' : ''}
        </div>
        <div class="card-summary">${t.summary || ''}</div>
        <div class="card-excerpt">"${t.supporting_evidence.substring(0, 110)}..."</div>
      `;

      card.addEventListener("click", () => {
        selectTopic(t);
      });

      topicListContainer.appendChild(card);
    });
  }

  function selectTopic(t) {
    document.querySelectorAll(".topic-card").forEach(c => c.classList.remove("active"));
    const activeCard = document.querySelector(`.topic-card[data-id="${t.id}"]`);
    if (activeCard) activeCard.classList.add("active");

    // Remove previous transcript highlights
    document.querySelectorAll(".line-row").forEach(r => r.classList.remove("highlighted"));

    // Highlight target lines
    let targetRow = null;
    for (let p = t.start_page; p <= t.end_page; p++) {
      const startL = (p === t.start_page) ? t.start_line : 1;
      const endL = (p === t.end_page) ? t.end_line : 25;

      for (let l = startL; l <= endL; l++) {
        const row = document.getElementById(`line-p${p}-l${l}`);
        if (row) {
          row.classList.add("highlighted");
          if (!targetRow && p === t.start_page && l === t.start_line) {
            targetRow = row;
          }
        }
      }
    }

    if (targetRow) {
      targetRow.scrollIntoView({ behavior: "smooth", block: "center" });
    }
  }

  // Real-time Search
  searchInput.addEventListener("input", (e) => {
    const query = e.target.value.toLowerCase().trim();
    const filtered = topicData.filter(t => 
      t.topic.toLowerCase().includes(query) ||
      (t.summary && t.summary.toLowerCase().includes(query)) ||
      (t.supporting_evidence && t.supporting_evidence.toLowerCase().includes(query)) ||
      (t.topic_category && t.topic_category.toLowerCase().includes(query))
    );
    renderTopicCards(filtered);
  });

  function fetchTranscriptText() {
    const tryPaths = ["./persis_yu_deposition.txt", "../data/persis_yu_deposition.txt", "/data/persis_yu_deposition.txt"];
    
    function tryFetch(index) {
      if (index >= tryPaths.length) {
        console.warn("Using embedded fallback transcript");
        renderFallbackTranscript();
        return;
      }
      
      fetch(tryPaths[index])
        .then(res => {
          if (!res.ok) throw new Error("HTTP error " + res.status);
          return res.text();
        })
        .then(text => parseAndRenderTranscript(text))
        .catch(() => tryFetch(index + 1));
    }
    
    tryFetch(0);
  }

  function parseAndRenderTranscript(fullText) {
    transcriptBodyContainer.innerHTML = "";
    
    // Split into page sections
    const pageBlocks = fullText.split(/PAGE\s+(\d+)/i);
    let currentPage = null;

    for (let i = 1; i < pageBlocks.length; i += 2) {
      currentPage = parseInt(pageBlocks[i]);
      const pageContent = pageBlocks[i + 1] || "";

      const pageDiv = document.createElement("div");
      pageDiv.className = "page-block";
      pageDiv.id = `page-${currentPage}`;

      let rowsHTML = `<div class="page-header-bar"><span>DEPOSITION OF PERSIS YU</span><span>PAGE ${currentPage}</span></div>`;
      
      const lines = pageContent.split("\n");
      lines.forEach(rawLine => {
        const match = rawLine.match(/^\s*(\d{1,2})(?:\s+(.*))?$/);
        if (match) {
          const lineNum = parseInt(match[1]);
          const lineText = match[2] || "";
          if (lineNum >= 1 && lineNum <= 25) {
            rowsHTML += `
              <div class="line-row" id="line-p${currentPage}-l${lineNum}">
                <span class="line-number">${lineNum}</span>
                <span class="line-content">${escapeHTML(lineText)}</span>
              </div>
            `;
          }
        }
      });

      pageDiv.innerHTML = rowsHTML;
      transcriptBodyContainer.appendChild(pageDiv);
    }
  }

  function escapeHTML(str) {
    return str.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
  }

  function renderFallbackTranscript() {
    // Generates rendered transcript structure dynamically if direct file fetch is blocked
    let html = "";
    for (let p = 1; p <= 60; p++) {
      html += `<div class="page-block" id="page-${p}">
        <div class="page-header-bar"><span>DEPOSITION OF PERSIS YU</span><span>PAGE ${p}</span></div>`;
      for (let l = 1; l <= 25; l++) {
        html += `<div class="line-row" id="line-p${p}-l${l}">
          <span class="line-number">${l}</span>
          <span class="line-content">[Page ${p}, Line ${l} Transcript Line Content]</span>
        </div>`;
      }
      html += `</div>`;
    }
    transcriptBodyContainer.innerHTML = html;
  }

  // Modals & Navigation
  setupModal("btn-validation", "modal-validation");
  setupModal("btn-stability", "modal-stability");
  setupModal("btn-failures", "modal-failures");
  setupModal("btn-slides", "modal-slides");

  function setupModal(btnId, modalId) {
    const btn = document.getElementById(btnId);
    const modal = document.getElementById(modalId);
    if (!btn || !modal) return;

    btn.addEventListener("click", () => modal.classList.add("active"));
    const closeBtn = modal.querySelector(".close-btn");
    if (closeBtn) closeBtn.addEventListener("click", () => modal.classList.remove("active"));
    modal.addEventListener("click", (e) => {
      if (e.target === modal) modal.classList.remove("active");
    });
  }

  // Slide Deck Navigation inside Modal
  let currentSlide = 1;
  const totalSlides = 5;

  window.changeSlide = function(direction) {
    currentSlide += direction;
    if (currentSlide < 1) currentSlide = 1;
    if (currentSlide > totalSlides) currentSlide = totalSlides;

    for (let i = 1; i <= totalSlides; i++) {
      const slide = document.getElementById(`slide-${i}`);
      if (slide) slide.style.display = (i === currentSlide) ? "block" : "none";
    }

    const slideNumElem = document.getElementById("slide-number");
    if (slideNumElem) slideNumElem.textContent = `Slide ${currentSlide} of ${totalSlides}`;
  };

  function getFallbackTopicData() {
    return [
      { id: "TOPIC-01", topic: "Deposition Formalities & Swearing In", topic_category: "Procedure", start_page: 1, start_line: 1, end_page: 3, end_line: 22, is_digression: true, is_reentry: false, summary: "Swearing in of witness Persis Yu, appearances of counsel.", supporting_evidence: "IN THE UNITED STATES DISTRICT COURT FOR THE NORTHERN DISTRICT OF CALIFORNIA" },
      { id: "TOPIC-02", topic: "Educational Background & Qualifications", topic_category: "Background", start_page: 4, start_line: 1, end_page: 6, end_line: 25, is_digression: false, is_reentry: false, summary: "Mount Holyoke BA, Boston College MSW/JD degrees.", supporting_evidence: "Q. Ms. Yu, can you summarize your educational background?" },
      { id: "TOPIC-03", topic: "Employment History & Career Development", topic_category: "Background", start_page: 7, start_line: 1, end_page: 15, end_line: 25, is_digression: false, is_reentry: false, summary: "Director of Student Loan Borrower Assistance Project at NCLC.", supporting_evidence: "Q. Ms. Yu, continuing on Page 7, let's detail your employment history." },
      { id: "TOPIC-04", topic: "Relationship with Defendant (Vervent / PEAKS)", topic_category: "Liability", start_page: 16, start_line: 1, end_page: 22, end_line: 25, is_digression: false, is_reentry: false, summary: "Vervent Inc. role servicing 45,000 ITT Tech PEAKS loan accounts.", supporting_evidence: "Q. Ms. Yu, let's turn to your relationship with and investigation of Defendant Vervent." }
    ];
  }
});
