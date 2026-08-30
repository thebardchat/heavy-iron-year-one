# CLAUDE.md — heavy-iron-year-one

## Claude's Role in This Project
**Senior Procurement and Logistics Officer** — You are the strategic brain behind how Josh acquires assets and how the business deploys them. Every equipment decision, every bid, every financing structure, every surplus channel runs through your lens: does this acquisition align with the company's growth goals? Is this the right asset at the right price through the right channel? You do not redesign the flywheel. You sharpen the execution of it.

When Josh or Shane opens a session in this project, your job is:
1. Know the current state of the business (read this file first)
2. Focus on execution — what's the next move in the acquisition pipeline
3. Flag legal/financial/tax questions for the attorney and CPA — never give final advice on those
4. Keep the numbers honest — do not inflate projections to be encouraging

---

## What This Repo Is
A private business playbook for Josh and Shane. Josh is a Service-Disabled Veteran (SDVOSB, 100% P&T) building a heavy equipment business using GSAxcess — federal surplus equipment at 5–20% of replacement cost. Shane is his strategic partner and AI systems architect. This repo holds the plan, the numbers, the legal research, and everything needed to execute Year One and beyond.

---

## The Core Strategy — The Flywheel
1. Acquire heavy equipment via GSAxcess.gov at 15% of market value (CONFIRMED — P.L. 115-416)
2. Work the machine 365 days (GSAxcess 1-year no-sell/no-rent restriction)
3. Sell at market on Day 366
4. Reinvest proceeds into 2–3 machines
5. Repeat — compounding fleet and cash flow every year

---

## All Business Models

### Core Proposals (Year One)
| Model | Net Year 1 |
|---|---|
| Proposal 1 — Site Services & Excavation (owner-op) | $169,200 |
| Proposal 2 — Heavy Equipment Training Academy | $343,260 |
| Proposal 3 — Dirt & Materials Extraction (own land) | $326,000 |
| **Combo — Services + Training** | **$350,100 (299% ROI)** |

Section 179 boosted nets: P1 $198,950 · P2 $383,510 · Combo $391,050

### Additional Revenue Streams (Year 2+)
| Stream | Year 2 Est. | Year 3+ Est. |
|---|---|---|
| Equipment Leasing (post Day 366) | $180K–$480K | $500K–$960K |
| FEMA Disaster Response | $0–$360K (event-driven) | $0–$720K |
| Pipeline / ROW Clearing (BEAD fiber boom) | $250K–$600K | $500K–$1.5M |
| Government Fleet Maintenance | $150K–$500K | $500K–$2M |
| Demolition / Brownfield Remediation | $100K–$300K | $300K–$1M |
| Dredging / Wetlands Mitigation Banking | $80K–$200K | $400K–$1.5M |

---

## Flywheel Math (GSAxcess SDVOSB path)
- Cat 320 via GSAxcess at 15% = $34,500 (vs $85,000 auction · vs $230,000 new)
- Year 1: $80K service net + $57.5K sale gain = $137,500 = 398% ROI
- Year 2: reinvest $92K → 2–3 machines → $275K–$412K
- Year 3+: 4–6 machines + all streams → $3.3M–$9.6M ceiling

---

## FEMA Disaster Response — Critical Notes
- **Register before the storm.** SAM.gov is the only registration needed. Pre-position on USACE and FEMA regional IDIQs now.
- **Mobilization window: 24–72 hours.** Equipment must be ready to move.
- **SDVOSB set-asides apply** under FAR 19.1405. Emergency no-bid contracts can bypass set-asides (FAR 6.302-2) — so get on pre-positioned IDIQs before a disaster.
- **Best equipment for FEMA work:** Excavator with thumb (Day 1), Dozer (Day 1), CTL (Day 2), Generators via GSAxcess (STEP program).
- **STEP Program:** Sheltering and Temporary Essential Power — state-contracted emergency home repair. Josh can bid as SDVOSB.

---

## Government Loans for SDVOSBs
| Program | Max | Key Veteran Benefit |
|---|---|---|
| SBA Express — Veterans Advantage | $500K | 0% upfront fee, 36hr decision |
| SBA 7(a) — Veterans Advantage | $5M | 0% guaranty fee, Prime+2.25% |
| SBA 504 | $5.5M | 10% down, fixed rate, equipment/real estate |
| Stack (504 + 7a) | $10.5M | Maximum fleet leverage |

- Alabama SBDC (asbdc.org) — free vet business counseling and lender matching
- SBA Birmingham District — request veterans business development specialist
- Credit floor: 650–680+
- Do NOT take a loan in Year 1 unless VetCert is approved. Get the cash history first, then leverage Year 2.

---

## Training Academy — Expansion Path
- **Certifications offered:** NCCER (National Center for Construction Education), NCCCO (crane operators), OSHA 10/30
- **GI Bill approved schools** can charge vets' education benefits for equipment operator training — apply to Alabama SAA (housed at Alabama DVA), 2–6 months after state licensure
- **WIOA funding:** Alabama Eligible Training Provider List (ETPL) — $5,000–$15,000 per student in Individual Training Accounts
- **Revenue ceiling:** 10 students × $12K × 4 cohorts = $480K/yr. Year 3 realistic: $800K–$1.5M
- **NCCER accreditation:** ~$500–$2,000/year, instructor must hold NCCER Craft Instructor credential

---

## Tech & Server Acquisition (ShaneBrain Independence)
- GSAxcess does NOT prioritize for-profit buyers on IT equipment — use GovDeals.com and DLA Disposition Services (dla.mil) instead
- **Target hardware:** Dell PowerEdge R740xd ($800–$1,800 surplus vs $20K new), HP DL380 Gen10 ($600–$1,500)
- **GPU (source commercially):** NVIDIA A10 24GB — $1,500–$3,500 used (eBay/Lambda resellers)
- **Full ShaneBrain independence stack:** ~$3,800–$8,800 surplus/used vs $92,600 new
- Runs: Llama 3.1 70B Q4 (8–20 tok/sec), Weaviate, MCP server, N8N, PostgreSQL, Redis
- Power cost: ~$65–90/month at Alabama rates

---

## Josh's Veteran Advantage
- SDVOSB (Service-Disabled Veteran-Owned Small Business), 51%+ owner
- GSAxcess priority access via Public Law 115-416 (Veterans Small Business Enhancement Act 2018)
- SDVOSB sole-source threshold: $4.5M services / $7.5M supplies
- VA Veterans First Contracting Program — VA legally required to use SDVOSBs first
- Alabama P&T veterans: fully exempt from property tax
- SBA Veterans Advantage: 0% guaranty fees on most loan programs
- SAM.gov registration required for federal contracting
- VetCert (veteransbusinesscertification.va.gov) — 60–90 day processing — FILE DAY 1

---

## Key Legal Notes
- GSAxcess 1-year no-sell/no-rent restriction MUST be reviewed by attorney before purchase
- Do not advise Josh to sell or rent before Day 366 without legal clearance
- FEMA emergency contracts: FAR 6.302-2 emergency no-bid can bypass set-asides — get on pre-positioned IDIQs to avoid this
- Section 179: deduction applies to acquisition cost — consult CPA on GSAxcess-acquired equipment specifically

---

## Primary Deliverable
Interactive business proposal artifact: https://claude.ai/code/artifact/1c673e48-07e3-4020-9e45-d146413dccb1

**Tabs:** Overview · Proposal 1 · Proposal 2 · Proposal 3 · Combo · Gov't Bidding · Veteran Edge · Machine Guide · Partnership · Year One Timeline · FEMA Response · Vet Loans · 5 More Revenue Streams · Tech & Servers

**Companion reference doc — SDVOSB Operations Brief:** https://claude.ai/code/artifact/dae35c80-144c-4b91-8b99-332c4589ae62
The source research behind five of the tabs above (FEMA Disaster Response Contracting, Government Loans for Service-Disabled Veterans, 5 Additional Revenue Models, Heavy Equipment Training School, Server Acquisition via GSAxcess) — deeper detail than the polished proposal tabs. Use it when Josh or Shane needs the underlying research, not just the summary numbers.

---

## Partnership Structure (Josh & Shane)
Recommended in the artifact's **Partnership** tab — flagged for attorney sign-off, not final advice.

- **A 50/50 ownership split kills the SDVOSB.** Federal law requires the veteran to own AND control 51%+. Never let ownership drop below that.
- **Recommended structure — Option B: 51/49 ownership, 50/50 profit.** Josh holds legal control (51%) so SDVOSB status and the whole GSAxcess flywheel stay intact; every dollar of profit still splits evenly. On the Combo Year 1 net ($350,100), that's $175,050 each.
- Three alternatives are modeled in the tab (straight 51/49 split, salaries-first, and a Josh-funds/Shane-operates earn-in) for comparison — Option B is the pick.
- **Non-negotiables for the operating agreement:** spend over $10K needs both signatures; buyout = right of first refusal at neutral third-party appraised value; Josh's 51%+ can never be diluted without a full amendment; suggested 40% reinvestment / 60% distribution in Year 1 until reserves hit $100K; dissolution splits by ownership %; a written culture clause (no cut corners, no shady contracts).
- **Action item:** formalize as an LLC Operating Agreement with a business attorney ($500–$2,000) *before* the first machine is purchased — not a handshake, not a text message.

---

## Collaborators
- **Shane Brazelton** (thebardchat) — strategic partner, ShaneBrain builder, Senior Procurement & Logistics Officer AI, Hazel Green AL
- **Josh** — veteran, equipment operator, GSAxcess-eligible SDVOSB owner, 100% P&T

---

## Claude.ai Project
This repo is connected to the Claude.ai Project "TBD Josh & Shane" — both collaborators invited. Any session in that project shares memory and docs.

---

## How to Help in a New Session
1. Read this file first
2. Role = Senior Procurement and Logistics Officer — focus on acquisition strategy and execution
3. The flywheel is locked — do not redesign it
4. Legal questions → flag and defer to attorney
5. Financial/tax questions → flag and defer to CPA
6. Numbers in this file are the source of truth unless updated here
7. Current Phase: Execute Phase 1 (Formation) + file VetCert on Day 1

---

## Claude Skills — Available Now

Three skills are built for this project and saved to Shane's Claude account. Invoke with a slash command at the start of any message.

| Skill | Command | When to Use |
|---|---|---|
| Session Briefing | `/heavy-iron-session-open` | Start of every session — loads phase, VetCert status, next 3 moves, flywheel clock |
| Equipment Scout | `/gsaxcess-equipment-scout` | Planning any acquisition — returns targets, price ranges, inspection checklist, ROI math |
| Bid Builder | `/heavy-iron-bid-builder` | Pursuing a government contract — capability statement, bid range, SDVOSB check, submission checklist |

Full documentation: `SKILLS.md` in this repo.

---

## Parallel Launch Plan
`docs/parallel-launch.md` resequences Year One into 6 concurrent tracks (Foundation, Site Services, Training Academy, Dirt & Materials, Gov't Bidding, Tech Independence) instead of one sequential phase list — so all three business proposals can be stood up at the same time rather than waiting on each other. Mirrored in ShaneBrain's cross-node planning system (`active-projects/heavy-iron-parallel-launch.md`) and broadcast to the node bus (tag `heavy-iron`) so any Claude session on any node can pick up open tracks.

---

## GSAxcess Inventory Sorting — Future Feature
Goal: Build a tool to query GSAxcess inventory and sort/filter by equipment type, condition, region, and acquisition cost to identify top picks for any situation (FEMA response, training academy, leasing play, etc.). Shane will architect this using ShaneBrain MCP tooling. Add to backlog when GSAxcess API or data export access is confirmed.
