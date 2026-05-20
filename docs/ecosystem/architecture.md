# Pumpnetic — Ecosystem Architecture

Technical and structural overview of the Pumpnetic internet-native crypto ecosystem.

---

## Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                      PUMPNETIC ECOSYSTEM                            │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                  ECOSYSTEM LAYER                            │   │
│   │  pumpnetic.com · docs.pumpnetic.com · GitHub Public Repo   │   │
│   └─────────────────────────────────────────────────────────────┘   │
│                              │                                      │
│        ┌─────────────────────┼──────────────────────┐              │
│        ▼                     ▼                      ▼              │
│  ┌───────────┐        ┌────────────┐         ┌───────────┐         │
│  │   $NSGC   │        │   $NOALC   │         │  $IKWYD   │         │
│  │           │        │            │         │           │         │
│  │ nsgc.     │        │ noalc.     │         │ ikwyd.    │         │
│  │ pumpnetic │        │ pumpnetic  │         │ pumpnetic │         │
│  │ .com      │        │ .com       │         │ .com      │         │
│  └───────────┘        └────────────┘         └───────────┘         │
│        │                     │                      │              │
│        └─────────────────────┼──────────────────────┘              │
│                              ▼                                      │
│   ┌─────────────────────────────────────────────────────────────┐   │
│   │                  BNB SMART CHAIN                            │   │
│   │           EVM-Compatible · BEP-20 Standard                  │   │
│   │      PancakeSwap V2 AMM · BSCScan Verified Contracts        │   │
│   └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Infrastructure Layers

### 1. Ecosystem Layer

The ecosystem layer is the coordination and branding infrastructure:

- **`pumpnetic.com`** — main ecosystem portal
- **`docs.pumpnetic.com`** — official documentation portal
- **`github.com/pumpneticprojects-collab/pumpnetic-public`** — public repo (source of truth for documentation, assets, contracts)
- **`@pumpnetic`** — unified ecosystem X account

### 2. Project Layer

Each project operates as an independent internet-native brand:

| Project | Subdomain | X Account | Telegram |
|---|---|---|---|
| $NSGC | `nsgc.pumpnetic.com` | `@NoSugarCoin` | `t.me/NoSugarCoin` |
| $NOALC | `noalc.pumpnetic.com` | `@NoalcCoin` | `t.me/NOALCcoin` |
| $IKWYD | `ikwyd.pumpnetic.com` | `@IKWYDCoin` | `t.me/IKWYDCoin` |

### 3. On-Chain Layer

All tokens are deployed on **BNB Smart Chain (BSC)** using the BEP-20 standard:

| Token | Contract Address | Supply | Tax |
|---|---|---|---|
| `$NSGC` | `0x19B1b3C12642Cc08B73e6b03e52841004dc5E299` | 100,000,000 | 0/0% |
| `$NOALC` | `0xa223dC6241Ab785b3EA81318B098E06BD6527158` | 1,000,000,000 | 0/0% |
| `$IKWYD` | `0xA3ad36133013Db657107266c18cbe1aea0319821` | 1,000,000,000 | 0/0% |

---

## Technical Standards

### Token Implementation

All Pumpnetic tokens follow these implementation principles:

- **BEP-20 Standard** — fully ERC-20 compatible, verifiable against the BEP-20 specification
- **OpenZeppelin Base** — using battle-tested, audited contract patterns
- **Fixed Supply** — total supply minted at deployment, no mint functions post-launch
- **Zero Tax** — 0% buy tax, 0% sell tax — no hidden fees or transfer conditions
- **No Blacklists** — no transfer-blocking, no address blacklisting, no honeypot vectors
- **BscScan Verified** — all contracts have verified source code, readable by anyone

### Verification Protocol

> All claims in this documentation can and should be independently verified on-chain.

For each token, you can verify:
1. **Contract source** — BscScan → Contract → Code tab
2. **Supply** — BscScan → Token Tracker
3. **Tax** — BscScan → Contract → Read Contract → `_taxFee` / transfer logic
4. **Liquidity lock** — check LP token holder on BscScan, verify lock contract
5. **Ownership** — BscScan → Contract → Read Contract → `owner()`

### Subdomain Infrastructure

```
*.pumpnetic.com   →   Cloudflare Workers (edge-deployed)
pumpnetic.com     →   Main portal
docs.pumpnetic.com →  Documentation portal
```

---

## Documentation Standard

Every Pumpnetic project publishes a standardized documentation set:

```
docs/projects/<project>/
├── <project>.md             ← Primary doc (overview, token info, links)
└── whitepaper/
    └── <PROJECT>_WhitePaper.pdf   ← Full technical + narrative whitepaper
```

This ensures any exchange, aggregator, or auditor checking the public repo finds a consistent, complete, and verifiable information set for every project.

---

## Asset Standard

```
assets/<project>/
├── <project>-bscscan-32x32.png    ← BSCScan token icon (32px)
├── <project>-bscscan-64x64.png    ← BSCScan token icon (64px)
├── <project>-bscscan-128x128.png  ← BSCScan token icon (128px)
├── <project>-bscscan-256x256.png  ← BSCScan token icon (256px)
├── <project>-bscscan-512x512.png  ← BSCScan token icon (512px)
└── <project>-logo-32x32.svg       ← Vector logo
```

All assets are served via raw GitHub URLs for direct reference in token listings, documentation, and third-party integrations.

---

## Ecosystem Contacts

| Entity | Email |
|---|---|
| Pumpnetic (Ecosystem) | info@pumpnetic.com |
| No Sugar Coin | nsgc@pumpnetic.com |
| No Alcohol Coin | noalc@pumpnetic.com |
| I Know What You Did | ikwyd@pumpnetic.com |

---

<div align="center">

*© 2026 Pumpnetic. Built on the Internet.*

[pumpnetic.com](https://pumpnetic.com) · [docs.pumpnetic.com](https://docs.pumpnetic.com)

</div>
