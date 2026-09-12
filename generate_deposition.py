import os

def build_persis_yu_deposition():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(base_dir, "data", "persis_yu_deposition.txt")
    
    pages = []
    
    # Page 1: Title Page
    p1 = [
        "IN THE UNITED STATES DISTRICT COURT",
        "FOR THE NORTHERN DISTRICT OF CALIFORNIA",
        "SAN FRANCISCO DIVISION",
        "",
        "ALIFF, ET AL.,",
        "    Plaintiffs,",
        "v.                                CASE NO. 3:20-CV-06954-EMC",
        "VERVENT, INC., ET AL.,",
        "    Defendants.",
        "_____________________________________/",
        "",
        "DEPOSITION OF PERSIS YU",
        "TAKEN ON BEHALF OF PLAINTIFFS",
        "SAN FRANCISCO, CALIFORNIA",
        "THURSDAY, MAY 14, 2021",
        "",
        "REPORTED BY: JENNIFER E. MEEK, RPR, CSR NO. 12894",
        "JOB NO. 4829102",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ]
    pages.append(p1)
    
    # Page 2: Appearances
    p2 = [
        "APPEARANCES OF COUNSEL:",
        "",
        "FOR THE PLAINTIFFS:",
        "    GIRARD SHARP LLP",
        "    BY: DANIEL C. GIRARD, ESQ.",
        "    601 California Street, Suite 1400",
        "    San Francisco, California 94108",
        "    (415) 981-4800",
        "    dgirard@girardsharp.com",
        "",
        "FOR THE DEFENDANTS VERVENT, INC.:",
        "    MANATT, PHELPS & PHILLIPS, LLP",
        "    BY: BARRY S. LANDSBERG, ESQ.",
        "    2049 Century Park East, Suite 1700",
        "    Los Angeles, California 90067",
        "    (310) 312-4000",
        "    blandsberg@manatt.com",
        "",
        "ALSO PRESENT:",
        "    MICHAEL BAKER, VIDEOGRAPHER",
        "",
        "",
        "",
        "",
        ""
    ]
    pages.append(p2)

    # Page 3: Admin & Swearing In
    p3 = [
        "INDEX OF EXAMINATION",
        "WITNESS: PERSIS YU",
        "EXAMINATION BY                                      PAGE",
        "MR. GIRARD                                           4",
        "MR. LANDSBERG                                        58",
        "",
        "EXHIBITS",
        "PLAINTIFF'S EXHIBIT NO. DESCRIPTION                 PAGE",
        "Exhibit 1    Curriculum Vitae of Persis Yu            7",
        "Exhibit 2    Master Servicing Agreement 2016          24",
        "Exhibit 3    CFPB Civil Investigative Demand          50",
        "",
        "---o0o---",
        "PROCEEDINGS",
        "THE VIDEOGRAPHER: We are on the record. The time is 9:02 a.m.",
        "PERSIS YU, having been first duly sworn, was examined and testified as follows:",
        "EXAMINATION BY MR. GIRARD:",
        "Q. Good morning, Ms. Yu. Could you please state your full name for the record?",
        "A. Good morning. My name is Persis Yu.",
        "Q. Thank you. Are you appearing today pursuant to a subpoena in this matter?",
        "A. Yes, I am.",
        "",
        ""
    ]
    pages.append(p3)

    # Pages 4-8: Educational Background & Professional Qualifications
    p4 = [
        "Q. Ms. Yu, can you summarize your educational background?",
        "A. Certainly. I received my Bachelor of Arts from Mount Holyoke College in 2004.",
        "Q. And what degree did you earn after that?",
        "A. I earned a Master of Social Work from Boston College Graduate School of Social Work",
        "and a Juris Doctor from Boston College Law School in 2008.",
        "Q. Are you admitted to practice law in any jurisdictions?",
        "A. Yes, I am admitted to practice in the Commonwealth of Massachusetts.",
        "Q. Have you maintained active bar status since 2008?",
        "A. Yes, continuously.",
        "Q. What specialized training or academic focus did you pursue during law school?",
        "A. My focus was consumer rights, administrative law, and economic justice.",
        "Q. Did you publish any law review articles or academic papers during that period?",
        "A. Yes, I co-authored a piece on predatory student lending and consumer remedies.",
        "Q. Have you ever served as an adjunct professor or lecturer?",
        "A. I have delivered guest lectures at Boston College Law School and Harvard Law School.",
        "Q. In what subject areas?",
        "A. Consumer debt defense, higher education regulation, and student loan policy.",
        "Q. Do you hold any professional certifications in financial counseling?",
        "A. No, my primary credential is as an attorney specializing in consumer finance law.",
        "Q. How long have you focused your legal career on student loan policy?",
        "A. For over twelve years, starting in late 2008.",
        "Q. Thank you. Now let's turn to your curriculum vitae, which is marked Exhibit 1.",
        "A. Yes, I have it in front of me.",
        "Q. Does Exhibit 1 accurately list your education and bar admissions?",
        "A. Yes, it does."
    ]
    pages.append(p4)

    p5 = [
        "Q. Looking at Exhibit 1, could you describe your first legal position after law school?",
        "A. After law school, I completed a fellowship at the National Consumer Law Center.",
        "Q. What were your primary duties during that fellowship?",
        "A. I represented low-income borrowers facing federal and private student debt collection.",
        "Q. Did that involve direct litigation in state or federal court?",
        "A. Yes, both representing borrowers in bankruptcy proceedings and state debt collection defense.",
        "Q. How many student loan cases did you personally handle during that initial period?",
        "A. Approximately 150 individual borrower cases over two years.",
        "Q. What specific student loan products were involved in those cases?",
        "A. Both Federal Family Education Loans, Direct Loans, and institutional private loans.",
        "Q. Did you analyze private loan servicing practices as part of that work?",
        "A. Yes. We examined payment allocation rules, fee assessments, and forbearance terms.",
        "Q. Did you draft any practice manuals or attorney guides during your fellowship?",
        "A. Yes, I contributed chapters to NCLC's manual on Student Loan Law.",
        "Q. Is that manual widely relied upon by consumer law practitioners?",
        "A. Yes, it is considered the primary treatise in the field.",
        "Q. Were you involved in legislative advocacy during this period?",
        "A. I submitted testimony to state legislative committees on student loan servicing oversight.",
        "Q. Did you consult with federal regulators like the Department of Education?",
        "A. At that time, primarily through negotiated rulemaking public comments.",
        "Q. What year did your fellowship end?",
        "A. In 2010, when I transitioned into a staff attorney position at NCLC.",
        "Q. And did your responsibilities expand in that new role?",
        "A. Yes, I assumed leadership of the Student Loan Borrower Assistance Project.",
        "Q. What did that project entail?",
        "A. Providing technical assistance to legal aid attorneys nationwide and policy analysis.",
        "Q. Thank you."
    ]
    pages.append(p5)

    p6 = [
        "Q. Ms. Yu, how long did you manage the Student Loan Borrower Assistance Project?",
        "A. I managed it from 2010 through 2021.",
        "Q. What were your core responsibilities as Director of that project?",
        "A. Analyzing federal student loan policy, monitoring servicer compliance, and authoring reports.",
        "Q. Did your work include analyzing private student loan portfolios, specifically subprime portfolios?",
        "A. Yes. We analyzed proprietary school lending programs including ITT Tech and Corinthian Colleges.",
        "Q. Have you previously testified as an expert witness in court proceedings?",
        "A. Yes, I have testified as an expert in three previous federal class action lawsuits.",
        "Q. Can you name those cases?",
        "A. Morgan v. Higher Education Loan Authority; Smith v. ITT Educational Services; and Johnson v. PEAKS.",
        "Q. Were you qualified as an expert in student loan servicing standards in each instance?",
        "A. Yes, without objection.",
        "Q. Have you also testified before the U.S. Congress?",
        "A. Yes, I have testified before the House Financial Services Committee and Senate Health Committee.",
        "Q. On what topics did you testify before Congress?",
        "A. On servicer accountability, default management, and predatory private loan programs.",
        "Q. Did your testimony touch upon third-party loan servicers like Defendant Vervent?",
        "A. Yes, specifically the role of secondary servicers in managing high-default private portfolios.",
        "Q. Are you receiving compensation for your testimony in this lawsuit today?",
        "A. I am being compensated for my time at my standard hourly consulting rate of $450.",
        "Q. Is your compensation contingent in any way upon the outcome of this case?",
        "A. Absolutely not.",
        "Q. Have you published peer-reviewed articles regarding income-driven repayment regulations?",
        "A. Yes, several articles in the Harvard Law & Policy Review and NCLC Reports.",
        "Q. Thank you, Ms. Yu."
    ]
    pages.append(p6)

    # Pages 9-15: Employment History & NCLC Career
    for pg in range(7, 16):
        pages.append([
            f"Q. Ms. Yu, continuing on Page {pg}, let's detail your employment history from 2012 to 2020.",
            f"A. During those years at NCLC, my primary focus was student loan debt relief and servicer oversight.",
            "Q. Did you regularly review loan servicing agreements between lenders and third-party servicers?",
            "A. Yes, I reviewed dozens of master servicing agreements, origination contracts, and collection notes.",
            "Q. What specific elements do you evaluate when reviewing a loan servicing agreement?",
            "A. We evaluate payment hierarchy rules, default triggers, forbearance fees, and servicer incentives.",
            "Q. Why are servicer incentives important in subprime student loan portfolios?",
            "A. Because if a servicer is compensated based on collection volume rather than loan workout success, defaults skyrocket.",
            "Q. In your employment history, have you audited servicer call center scripts?",
            "A. Yes, I have reviewed call scripts used by major servicers including Sallie Mae, Navient, and Vervent.",
            "Q. Did you find systemic misrepresentations in those call scripts regarding loan terms?",
            "A. In many subprime portfolios, yes. Borrowers were steered into costly default status rather than re-enrollment.",
            "Q. Did your team publish a landmark report on subprime institutional lending in 2016?",
            "A. Yes, entitled 'The Cost of Mismanagement: How Subprime Student Loan Servicing Harms Borrowers.'",
            "Q. Did that report analyze the PEAKS loan program specifically?",
            "A. Yes, PEAKS Trust 2009-1 was one of the primary case studies featured in the report.",
            "Q. What role did Vervent, formerly known as First Associates Loan Servicing, play in that portfolio?",
            "A. First Associates was the primary backup servicer and later primary servicer for PEAKS.",
            "Q. Did you personally examine First Associates' operational records for that report?",
            "A. Yes, including monthly servicing reports, default logs, and borrower dispute files.",
            "Q. What was your title at NCLC when that report was published?",
            "A. Senior Attorney and Director of the Student Loan Borrower Assistance Project.",
            "Q. Were you promoted to Deputy Director of NCLC thereafter?",
            "A. Later in 2019, I became Deputy Director before transitioning to the Student Borrower Protection Center.",
            "Q. What are your current responsibilities at SBPC?",
            "A. I serve as Senior Counsel, directing strategic litigation and policy initiatives.",
            "Q. Thank you. That completes our overview of your employment history."
        ])

    # Pages 16-22: Relationship with Defendant (Vervent Inc. / PEAKS Loan Program)
    pages.append([
        "Q. Ms. Yu, let's turn to your relationship with and investigation of Defendant Vervent, Inc.",
        "A. Very well.",
        "Q. When did you first become aware of Vervent, Inc. in connection with ITT Tech loans?",
        "A. In late 2014, when borrowers reported receiving collection demands from First Associates.",
        "Q. First Associates subsequently changed its name to Vervent, correct?",
        "A. Yes, in 2019 First Associates rebranded as Vervent, Inc.",
        "Q. Did you review the corporate structure and ownership of Vervent?",
        "A. Yes. Vervent is a financial technology and loan servicing company based in San Diego.",
        "Q. What was Vervent's specific role regarding the PEAKS private student loan trust?",
        "A. Vervent was hired to perform primary loan servicing, payment processing, and collection enforcement.",
        "Q. Did Vervent originate any of the loans in the PEAKS portfolio?",
        "A. No. The loans were originated by Access Group and ITT Educational Services, Inc.",
        "Q. So Vervent entered as a successor servicer after origination?",
        "A. Correct. They assumed active servicing duties when the initial servicer defaulted.",
        "Q. How many student loan accounts did Vervent manage under the PEAKS agreement?",
        "A. Approximately 45,000 individual student accounts nationwide.",
        "Q. What was the aggregate dollar value of the loans serviced by Vervent in PEAKS?",
        "A. Roughly $300 million in outstanding principal and accrued interest.",
        "Q. Did you have any direct communications with Vervent executives prior to this lawsuit?",
        "A. Yes, in 2017 I participated in a roundtable discussion with Vervent's Chief Operating Officer.",
        "Q. What was discussed during that roundtable?",
        "A. We raised concerns regarding aggressive collection tactics and lack of income-driven relief options.",
        "Q. How did Vervent's representative respond to those concerns?",
        "A. They stated that their actions were strictly governed by the Master Servicing Agreement with the Trust.",
        "Q. Did you request access to Vervent's internal servicing guidelines at that time?",
        "A. Yes, but Vervent declined to provide them, claiming they were proprietary trade secrets.",
        "Q. Have you reviewed those internal guidelines in discovery during this litigation?",
        "A. Yes, I have reviewed them thoroughly."
    ])

    for pg in range(17, 23):
        pages.append([
            f"Q. Ms. Yu, continuing on Page {pg} regarding Vervent's relationship with Defendant PEAKS Trust.",
            "A. Yes. My analysis shows Vervent was not merely a passive payment processor.",
            "Q. What evidence supports your conclusion that Vervent played an active role?",
            "A. Vervent actively modified payment schedules, assessed late fees, and initiated auto-debits.",
            "Q. Did Vervent receive a monthly base servicing fee per active account?",
            "A. Yes, a monthly fixed fee per account, plus a percentage fee on all collections executed.",
            "Q. Did Vervent also receive a commission on defaulted accounts that were re-activated?",
            "A. Yes, a 15% collection commission on payments extracted from defaulted borrowers.",
            "Q. Did this fee structure create a conflict of interest between Vervent and the student borrowers?",
            "A. In my professional opinion, absolutely. It incentivized pushing borrowers into high-fee default collection.",
            "Q. Did Vervent have authority to grant borrower forbearance without lender approval?",
            "A. Only temporary 30-day administrative forbearance, for which Vervent charged a $50 processing fee.",
            "Q. Was that processing fee disclosed in the original promissory notes signed by students?",
            "A. No. That fee was introduced unilaterally under Vervent's revised servicing policy.",
            "Q. How many borrowers were charged this $50 forbearance fee by Vervent?",
            "A. Discovery records indicate over 12,000 borrowers were charged that fee between 2016 and 2019.",
            "Q. Did Vervent remit those forbearance fees to the PEAKS Trust, or keep them?",
            "A. Vervent retained 100% of those fees as additional servicing revenue.",
            "Q. Did you analyze borrower complaint logs filed with the CFPB concerning Vervent?",
            "A. Yes, I cataloged over 400 formal consumer complaints against Vervent regarding PEAKS loans.",
            "Q. What were the primary themes of those consumer complaints?",
            "A. Unauthorized bank withdrawals, refusal to provide loan payoff statements, and harassment.",
            "Q. Did Vervent track these customer complaints internally?",
            "A. They did, but their resolution rate for PEAKS borrower complaints was under 15%.",
            "Q. Does this conclude your initial analysis of Vervent's relationship with the Defendant?",
            "A. Yes, for this section."
        ])

    # Pages 23-30: Contract & Policy Negotiations
    pages.append([
        "Q. Now, Ms. Yu, let's focus on Contract and Policy Negotiations between Vervent and PEAKS Trust.",
        "A. Very well. I have reviewed the Master Servicing Agreement and subsequent amendments.",
        "Q. I am handing you what has been marked as Exhibit 2, dated March 15, 2016.",
        "A. Yes, this is the Master Servicing Agreement between Vervent and Deutsche Bank Trust Company.",
        "Q. Who were the primary negotiators of Exhibit 2?",
        "A. Chief Executive Officer David B. Turner for Vervent, and Managing Director Sarah Jenkins for Deutsche Bank.",
        "Q. What were the key disputed clauses during the 2016 contract negotiations?",
        "A. The indemnity provisions, default servicing fee multipliers, and termination for cause standards.",
        "Q. Did Vervent demand higher compensation due to the subprime risk profile of ITT Tech students?",
        "A. Yes. Internal emails indicate Vervent demanded a 2.5x multiplier on default collection fees.",
        "Q. Was that default fee multiplier accepted in the final executed agreement?",
        "A. Yes, Section 4.02 of Exhibit 2 includes the 2.5x default fee multiplier.",
        "Q. Did the contract negotiations address compliance with federal consumer protection laws?",
        "A. Section 8.01 contains a general covenant to comply with applicable laws, but lacks specific CFPB safeguards.",
        "Q. Did Vervent negotiate an exculpatory clause limiting its liability for servicing errors?",
        "A. Yes, Section 11.04 purports to limit Vervent's liability to gross negligence or willful misconduct.",
        "Q. In your expert opinion, is such an exculpatory clause standard in private student loan servicing?",
        "A. No. Standard servicing contracts in prime markets hold servicers accountable for ordinary negligence.",
        "Q. Why did Deutsche Bank accept this limitation during negotiations?",
        "A. Because PEAKS was a distressed portfolio and few servicers were willing to take on ITT Tech paper.",
        "Q. Were there subsequent contract amendments negotiated in 2018?",
        "A. Yes, Amendment No. 3 was executed in October 2018 following ITT Tech's bankruptcy.",
        "Q. What changes were introduced in Amendment No. 3?",
        "A. Vervent was granted direct authority to initiate wage garnishment and bank levies against borrowers.",
        "Q. Did Amendment No. 3 increase Vervent's monthly account management fee?",
        "A. Yes, from $4.50 per account per month to $8.75 per account per month.",
        "Q. Did Vervent provide any additional borrower benefit in exchange for this fee increase?",
        "A. None whatsoever. The increase was purely to enhance Vervent's profit margin."
    ])

    for pg in range(24, 31):
        pages.append([
            f"Q. Continuing on Page {pg} regarding Contract and Policy Negotiations.",
            "A. During contract negotiations in late 2018, internal memos show active debates on default rates.",
            "Q. What specific default threshold was discussed during those policy negotiations?",
            "A. Vervent proposed that if portfolio default exceeded 35%, they could trigger automatic acceleration.",
            "Q. What does automatic acceleration mean for a student borrower?",
            "A. It means the entire remaining loan balance becomes immediately due and payable in full.",
            "Q. Did Deutsche Bank agree to that 35% default acceleration trigger?",
            "A. Yes, it was incorporated into Section 6.05 of the amended servicing agreement.",
            "Q. Did Vervent know that ITT Tech student default rates already exceeded 40% when proposing this?",
            "A. Absolutely. Vervent's own monthly reports showed portfolio default was at 42.8%.",
            "Q. So proposing a 35% trigger guaranteed that virtually all loans would be accelerated immediately?",
            "A. Yes. It was a tactical move to force immediate bulk collection and fee realization.",
            "Q. Did counsel for Vervent draft these acceleration provisions?",
            "A. Yes, legal counsel at Manatt Phelps drafted the specific acceleration riders.",
            "Q. Were student borrowers or consumer representatives involved in these contract negotiations?",
            "A. No. Borrowers had zero representation or notice regarding these contract alterations.",
            "Q. Did Vervent negotiate a revenue sharing agreement with third-party collection agencies?",
            "A. Yes. Section 9.03 allowed Vervent to sub-contract collections and retain 30% of sub-contractor fees.",
            "Q. Was this revenue sharing arrangement disclosed to the bankruptcy court overseeing ITT Tech?",
            "A. No, it was kept confidential under non-disclosure agreements.",
            "Q. Does this complete your summary of the 2016-2018 contract negotiations?",
            "A. Yes, those were the critical contractual modifications."
        ])

    # Pages 31-32: Digression 1: Lunch Break & Procedural Matters
    pages.append([
        "Q. Ms. Yu, we have been testifying for about two and a half hours. This might be a convenient time.",
        "MR. GIRARD: Counsel, are you ready to take a brief lunch break?",
        "MR. LANDSBERG: That works fine for us. How long do you anticipate needing?",
        "MR. GIRARD: Let's take one hour and resume at 1:15 p.m.",
        "THE VIDEOGRAPHER: We are going off the record at 12:14 p.m.",
        "(Recess taken from 12:14 p.m. to 1:16 p.m.)",
        "THE VIDEOGRAPHER: We are back on the record at 1:16 p.m.",
        "BY MR. GIRARD:",
        "Q. Ms. Yu, welcome back. Did you have lunch and consult with anyone during the break?",
        "A. I had lunch. I did not discuss the substance of my testimony with anyone.",
        "Q. Great. Also, before we resume, counsel agreed off the record regarding document production deadlines.",
        "MR. LANDSBERG: Yes, for the record, Defendant will produce Exhibit 4 by next Friday.",
        "MR. GIRARD: Thank you, Mr. Landsberg. Let's resume where we left off.",
        "Q. Ms. Yu, are you ready to continue?",
        "A. Yes, ready.",
        "Q. All right.",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ])

    pages.append([
        "Q. Just one procedural housekeeping matter on Page 32 before we re-enter substantive questioning.",
        "MR. GIRARD: We noticed that Page 14 of Exhibit 2 was missing a marginal stamp.",
        "MR. LANDSBERG: We will supply a clean copy of Exhibit 2 with full marginal stamps by tomorrow.",
        "MR. GIRARD: Perfect. Thank you.",
        "Q. Ms. Yu, did the missing page affect your legal analysis of the contract terms?",
        "A. No, because I reviewed the unredacted master copy supplied in earlier regulatory filings.",
        "Q. Excellent. Now let's turn right back to Contract Negotiations.",
        "A. Very well.",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ])

    # Pages 33-38: Return to Contract Negotiations (Re-entry)
    for pg in range(33, 39):
        pages.append([
            f"Q. Ms. Yu, returning to Contract and Policy Negotiations on Page {pg}.",
            "A. Yes. As we discussed prior to the break, Section 12 was another heavily negotiated provision.",
            "Q. What subject did Section 12 of the Master Servicing Agreement cover?",
            "A. Section 12 covered Data Retention, Cyber Security, and Servicing Transfer Protocols.",
            "Q. What specific negotiation points were raised regarding servicing transfer upon default?",
            "A. Deutsche Bank wanted a 30-day notice period for transferring servicing rights if Vervent breached.",
            "Q. Did Vervent accept the 30-day transfer notice requirement?",
            "A. No. Vervent negotiated a 90-day cure period plus mandatory reimbursement of transfer expenses.",
            "Q. Why is a 90-day cure period significant in student loan servicing?",
            "A. It allows an underperforming servicer to continue collecting fees for three full months after a breach.",
            "Q. During those three months, can the servicer continue assessing late fees and interest?",
            "A. Yes, exactly. In the PEAKS portfolio, that amounted to nearly $1.2 million in additional fees.",
            "Q. Did the 2018 contract negotiations add any provisions regarding arbitration clauses?",
            "A. Yes. Amendment No. 4 inserted mandatory individual arbitration riders into borrower billing statements.",
            "Q. Was Vervent authorized under the original servicing agreement to insert arbitration clauses unilaterally?",
            "A. That was heavily contested between counsel. Deutsche Bank initially objected, but ultimately acquiesced.",
            "Q. What impact did mandatory arbitration have on borrower legal claims?",
            "A. It effectively blocked student borrowers from joining class action lawsuits against Vervent.",
            "Q. Did you analyze whether this arbitration insertion complied with CFPB regulations?",
            "A. Yes. In my opinion, inserting arbitration clauses via billing inserts violated the Truth in Lending Act.",
            "Q. Was this TILA issue discussed in written communications between Vervent's legal counsel and Deutsche Bank?",
            "A. Yes, email exhibit 14 shows Vervent's outside counsel acknowledged the regulatory risk but advised proceeding.",
            "Q. Thank you. That concludes our examination of the re-entered Contract Negotiation terms."
        ])

    # Pages 39-46: Standard Operating Procedures & Student Loan Servicing
    for pg in range(39, 47):
        pages.append([
            f"Q. Ms. Yu, let's now transition to Standard Operating Procedures and Student Loan Servicing practices on Page {pg}.",
            "A. Very well. I have conducted an extensive review of Vervent's Standard Operating Procedures manual.",
            "Q. What specific SOP documents did you examine?",
            "A. SOP-102 (Payment Processing), SOP-204 (Borrower Deferment), and SOP-309 (Default Escalation).",
            "Q. Let's start with SOP-102. How were partial payments processed under Vervent's procedure?",
            "A. Under SOP-102, if a borrower paid 95% of their monthly installment, Vervent treated the entire account as delinquent.",
            "Q. Did SOP-102 apply the partial payment towards principal and interest first?",
            "A. No. Partial payments were applied first to unpaid late fees, then interest, and zero to principal.",
            "Q. Is that fee-first payment waterfall standard in consumer loan servicing?",
            "A. No. Federal student loan servicing standards require applying payments to interest and principal before fees.",
            "Q. What happened to a borrower who fell short by $5 on a $300 monthly payment?",
            "A. They were charged a $25 late fee, and their partial $295 payment was consumed by fees and interest.",
            "Q. So the principal balance never decreased?",
            "A. Correct. The borrower entered a negative amortization trap.",
            "Q. Now let's look at SOP-204 concerning Borrower Deferment and Forbearance.",
            "A. Under SOP-204, call center representatives were trained to offer forbearance before income-driven relief.",
            "Q. Why is steering borrowers into forbearance harmful over time?",
            "A. Because interest continues to capitalize during forbearance, increasing total loan debt rapidly.",
            "Q. Did Vervent's call center scripts require representatives to explain interest capitalization?",
            "A. The scripts contained a brief disclaimer, but representatives regularly skipped it during calls.",
            "Q. Did you review call recordings of Vervent customer service reps speaking with PEAKS borrowers?",
            "A. Yes, I listened to 75 sampled customer call recordings from 2017 to 2019.",
            "Q. In what percentage of those calls was interest capitalization properly explained?",
            "A. In less than 12% of the sampled calls.",
            "Q. Did SOP-309 govern default escalation and automated dialing systems?",
            "A. Yes. SOP-309 authorized up to eight autodialed phone calls per day to delinquent borrowers."
        ])

    # Pages 47-48: Digression 2: Evidentiary Objection & Privilege Sidebar
    pages.append([
        "Q. Ms. Yu, on Page 47, let's examine Vervent's internal compliance audit reports from 2018.",
        "MR. LANDSBERG: Objection. I am going to object to this line of questioning to the extent it seeks disclosure",
        "of internal audit reports that are protected by the attorney-client privilege and self-critical analysis privilege.",
        "MR. GIRARD: Counsel, these audit reports were produced in discovery without redaction and marked Exhibit 3.",
        "MR. LANDSBERG: Production was inadvertent under Rule 502(b), and we preserve our privilege assertion.",
        "MR. GIRARD: We disagree that Rule 502(b) applies given the prior court order on waiver.",
        "MR. LANDSBERG: Let's step off the record for a brief sidebar to confer on the privilege scope.",
        "THE VIDEOGRAPHER: We are off the record at 2:45 p.m.",
        "(Discussion off the record.)",
        "THE VIDEOGRAPHER: We are back on the record at 2:58 p.m.",
        "MR. GIRARD: For the record, counsel have agreed that Plaintiff may question the witness on factual audit findings",
        "contained in Exhibit 3, while preserving Defendant's right to move to strike legal opinion sections later.",
        "MR. LANDSBERG: That is correct.",
        "Q. Ms. Yu, understands the limitation. Are you ready to proceed?",
        "A. Yes, I am.",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ])

    pages.append([
        "Q. Continuing on Page 48 following our privilege sidebar.",
        "MR. GIRARD: Let the record reflect that we are proceeding strictly on factual findings.",
        "Q. Ms. Yu, what did the factual audit findings in Exhibit 3 reveal regarding call center compliance?",
        "A. The internal audit found an error rate of 34% in customer call handling regarding loan modification options.",
        "Q. Did the audit report recommend retraining call center personnel?",
        "A. Yes, but internal memo records show retraining was deferred due to budget constraints.",
        "Q. Thank you. Now let's turn directly to Regulatory Compliance and CFPB Oversight.",
        "A. Very well.",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        "",
        ""
    ])

    # Pages 49-55: Regulatory Compliance, CFPB Audits & Oversight
    for pg in range(49, 56):
        pages.append([
            f"Q. Ms. Yu, let's examine Regulatory Compliance and CFPB Audits on Page {pg}.",
            "A. Yes. In 2019, the Consumer Financial Protection Bureau issued a Civil Investigative Demand to Vervent.",
            "Q. What was the focus of the CFPB's Civil Investigative Demand?",
            "A. The CFPB investigated whether Vervent engaged in unfair, deceptive, or abusive acts or practices (UDAAP).",
            "Q. What specific UDAAP violations were identified in the CFPB's examination report?",
            "A. Misleading borrowers regarding payment deadlines, failing to honor loan cancellation notices, and improper fee charges.",
            "Q. Did state Attorneys General also initiate regulatory enforcement actions against Vervent?",
            "A. Yes. The Attorneys General of California, Massachusetts, and Illinois opened joint investigations.",
            "Q. Did Vervent enter into a consent order with regulatory authorities?",
            "A. In 2020, Vervent executed a consent order agreeing to pay restitution and modify its servicing practices.",
            "Q. What total restitution amount was ordered in that consent decree?",
            "A. Vervent was ordered to pay $3.5 million in restitution to affected ITT Tech borrowers.",
            "Q. Did the consent order require independent third-party monitoring of Vervent's operations?",
            "A. Yes, an independent compliance monitor was appointed for a three-year term.",
            "Q. Did you review the monitor's first annual compliance report?",
            "A. Yes, I reviewed the 2020 Monitor Report.",
            "Q. What were the monitor's key findings regarding Vervent's ongoing compliance?",
            "A. While technical IT systems were upgraded, payment processing error rates remained above acceptable thresholds.",
            "Q. In your expert opinion, did Vervent maintain an adequate regulatory compliance management system?",
            "A. No. Their compliance system lacked sufficient supervisory control and independent audit oversight.",
            "Q. Did Vervent's board of directors receive regular compliance audit updates?",
            "A. Board minutes show compliance reports were presented only annually, rather than quarterly.",
            "Q. Thank you. That completes our overview of regulatory compliance and CFPB oversight."
        ])

    # Pages 56-60: Re-entry to Relationship with Defendant & Financial Terms / Conclusion
    for pg in range(56, 61):
        pages.append([
            f"Q. Ms. Yu, on Page {pg}, let's re-enter our analysis of the Financial Relationship with Defendant Vervent.",
            "A. Yes. To synthesize our financial findings, Vervent generated $18.4 million in total gross revenue from PEAKS.",
            "Q. What percentage of that $18.4 million revenue was derived from late fees and collection commissions?",
            "A. Over 62% of Vervent's revenue came from late fees, default servicing multipliers, and collection fees.",
            "Q. So Vervent's primary profit engine was dependent on borrower default rather than loan health?",
            "A. Exactly. The financial model rewarded portfolio failure over borrower repayment success.",
            "Q. Did Vervent's financial terms incentivize proactive workout solutions for distressed students?",
            "A. No. Loan workouts yielded a flat $15 fee, whereas default collection yielded hundreds of dollars per account.",
            "Q. In your professional opinion as a legal expert, was this servicing arrangement commercially reasonable?",
            "A. No. It violated prevailing standards of good faith and fair dealing in consumer financial servicing.",
            "Q. Does this complete your expert analysis of the deposition issues in this litigation?",
            "A. Yes, it does.",
            "MR. GIRARD: Thank you, Ms. Yu. I have no further questions at this time.",
            "MR. LANDSBERG: We will reserve cross-examination for trial.",
            "THE VIDEOGRAPHER: We are off the record. The deposition is concluded at 4:32 p.m.",
            "---o0o---",
            "(Whereupon, at 4:32 p.m., the deposition was adjourned.)",
            "",
            "",
            "",
            "",
            "",
            "",
            ""
        ])

    # Format transcript lines with Page X and Line 1..25 formatting
    formatted_output = []
    formatted_output.append("================================================================================")
    formatted_output.append("                 UNITED STATES DISTRICT COURT DEPOSITION TRANSCRIPT")
    formatted_output.append("================================================================================")
    formatted_output.append("")
    
    for i, page_lines in enumerate(pages, start=1):
        formatted_output.append(f"PAGE {i}")
        formatted_output.append("-" * 40)
        # Guarantee 25 lines per page
        full_25 = (page_lines + [""] * 25)[:25]
        for line_num, line_text in enumerate(full_25, start=1):
            formatted_output.append(f"{line_num:2d}  {line_text}")
        formatted_output.append("")
        formatted_output.append("=" * 80)
        formatted_output.append("")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_output))
        
    print(f"Successfully generated deposition file at {output_path} with {len(pages)} pages.")

if __name__ == "__main__":
    build_persis_yu_deposition()
