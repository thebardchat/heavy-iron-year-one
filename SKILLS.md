# Heavy Iron Year One — Claude Skills

Three Claude skills are built specifically for this project. They are saved to Shane's Claude account and are available in any session inside the **TBD Josh & Shane** Claude project.

To invoke a skill, type the skill name as a slash command at the start of your message — for example `/heavy-iron-session-open`.

---

## `/heavy-iron-session-open`

**When to use:** Open every session with this. Any time you need a status update or want to know where the business stands.

**What it does:**
- Reads the current CLAUDE.md / Project docs to pull live state
- Returns a structured briefing: current phase, VetCert status, next 3 moves, open decisions, flywheel clock
- Asks one focused question to set the session's direction

**Example output:**
```
## Heavy Iron — Session Briefing [DATE]

Current Phase: Phase 2 — Insurance & Setup (Weeks 3–6)
VetCert Status: Filed — Day 45 of 60–90 day window
First Machine Target: Cat 320 Excavator — $34,500 target (15% of $230K new)
Revenue Model: Combo — Services + Training ($350,100 Year 1)

Next 3 Moves:
- [ ] Get general liability and equipment insurance quotes
- [ ] Build rate sheet for excavation services
- [ ] Arrange equipment storage location

Open Decisions:
- Attorney review of GSAxcess 1-year restriction — pending
- Business bank account — confirm opened

Flywheel Clock:
- Machine acquired: TBD
- Day 366 (sell date): TBD
- Year 1 net target: $80,000 service revenue
```

---

## `/gsaxcess-equipment-scout`

**When to use:** When planning any acquisition — whether for FEMA response, training academy, leasing, owner-op site work, or ShaneBrain tech servers.

**What it does:**
- Takes a mission type: `fema`, `training`, `leasing`, `owner-op`, or `tech`
- Returns a prioritized equipment target list with GSAxcess/GovDeals price ranges
- Runs flywheel acquisition math (buy price → Year 1 revenue → Day 366 sale → ROI)
- Returns a pre-buy inspection checklist (hours, undercarriage, hydraulics, transport cost)
- Routes IT/server acquisitions correctly to GovDeals.com and DLA — not GSAxcess

**Example trigger:** *"Scout equipment for FEMA response"* or *"What should we bid on at GSAxcess for the training academy?"*

**Key rule it enforces:** Tech/server acquisitions are NEVER routed through GSAxcess — federal IT surplus for for-profit buyers goes through GovDeals.com and DLA Disposition Services (dla.mil).

**Price benchmarks it uses:**
| Equipment | GSAxcess Target | Market Value | Day 366 Sale |
|---|---|---|---|
| Cat 320 Excavator | $25K–$45K | $85K–$120K | $75K–$105K |
| Dozer (Cat D6) | $20K–$40K | $70K–$100K | $60K–$90K |
| Compact Track Loader | $8K–$18K | $35K–$55K | $30K–$50K |
| Generator (STEP) | $2K–$8K | $15K–$30K | $12K–$25K |
| Dell R740xd Server | $400–$2,500 (GovDeals) | $15K–$22K new | — |

---

## `/heavy-iron-bid-builder`

**When to use:** When Josh has a specific government contract, SAM.gov opportunity, or bid to pursue. Also good for building the first capability statement before any specific bid.

**What it does:**
- Takes agency type, contract scope, and estimated value
- Identifies SDVOSB set-aside eligibility (VA = Veterans First mandatory; non-VA = FAR 19.1405; FEMA emergency = IDIQ pre-position is the play)
- Drafts a 1-page capability statement ready to send
- Estimates bid price range for Alabama market (site services, debris removal, training)
- Outputs a full bid submission checklist

**Output includes:**
- Capability statement draft (company name, core competencies, differentiators, NAICS codes, contact)
- Bid price range (don't undercut to win — protect margin)
- Submission checklist (SAM.gov active, VetCert, bonding, insurance certs, past performance)
- Legal/financial flags for attorney and CPA

**Example trigger:** *"Build a bid for USACE debris removal in North Alabama"* or *"Draft our capability statement for VA contracts"*

**Key rule it enforces:** Never advises signing a contract without attorney review. Always flags VetCert status.

---

## Notes for Josh

- These skills are Claude AI tools — they run inside the Claude.ai session, not as standalone apps
- They require being in the **TBD Josh & Shane** Claude project for full context
- Shane administers the skills — contact Shane to update or add new ones
- All legal and financial questions flagged by these skills go to the attorney and CPA — the skills do not give final advice on those

---

## Skill Administration

Skills are managed by Shane Brazelton via the Claude.ai interface.  
Repo: `thebardchat/heavy-iron-year-one` (or equivalent)  
Project: **TBD Josh & Shane** on Claude.ai — both collaborators invited.
