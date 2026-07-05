# Analytics Agent - Implementation Rules (EDIT ME)

This file is the agent's permanent memory. Everything here is applied to EVERY run.
Replace all examples with YOUR implementation. Add a new rule every time you correct the agent.

## Report Suite
- Company: <your_company_id>
- Report Suite: <your_reportsuite_prod>
- Default Segment: <s000_your_segment_id>  ← apply to every report unless told otherwise

## Critical dimension rules (examples - replace with yours)
- Platform split: use eVar7, NOT mobiledevicetype
  - eVar7 = "website" → web traffic
  - everything else → app traffic
- Market split: use eVar5 (locale, e.g. en-GB, de-DE)

## Variable map (your SDR - the more you add, the smarter every run gets)
- eVar5 = Market locale
- eVar7 = Platform identifier
- <add every eVar/prop/event your team actually uses>

## Known data quirks
- Push notification OPEN/SEND events inflate page views - exclude from content analysis
- <add quirks your team has learned the hard way>
