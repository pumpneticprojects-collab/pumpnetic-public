"""
================================================================================
NO SUGAR COIN ($NSGC) — WHITEPAPER BUILD SCRIPT
Pumpnetic Ecosystem · BNB Smart Chain
================================================================================
Run:  python build_nsgc_wp.py
Output: /mnt/user-data/outputs/NSGC_WhitePaper_v2.pdf
================================================================================
"""

import importlib.util, os

_here = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    'wp_template', os.path.join(_here, 'pumpnetic_wp_template.py'))
T = importlib.util.module_from_spec(spec)
spec.loader.exec_module(T)

# ══════════════════════════════════════════════════════════════════════════════
# PROJECT CONFIG
# ══════════════════════════════════════════════════════════════════════════════
T.PROJECT.update({
    'name':           'No Sugar Coin',
    'ticker':         '$NSGC',
    'tagline':        'The Discipline Token',
    'quote':          '"Modern society runs on sugar. We run on discipline."',
    'ecosystem':      'Pumpnetic Ecosystem',
    'network':        'BNB Smart Chain',
    'supply':         '100,000,000',
    'tax':            '0%',
    'standard':       'BEP-20',
    'compiler':       'Solidity v0.8.34',
    'contract':       '0x19B1b3C12642Cc08B73e6b03e52841004dc5E299',
    'owner':          '0x1695DC0E70D012e9b4d583Bd8667323991BdaA14',
    'website':        'https://nsgc.pumpnetic.com',
    'ecosystem_site': 'https://pumpnetic.com',
    'bscscan':        'https://bscscan.com/token/0x19B1b3C12642Cc08B73e6b03e52841004dc5E299',
    'telegram':       'https://t.me/NoSugarCoin',
    'twitter':        'https://x.com/NoSugarCoin',
    'email':          'nsgc@pumpnetic.com',
    'github':         'https://github.com/pumpneticprojects-collab/pumpnetic-public/blob/main/docs/projects/nsgc/nsgc.md',
    'output':         '/mnt/user-data/outputs/NSGC_WhitePaper_v2.pdf',
    'author':         'NodeFounder / Pumpnetic',
    'subject':        '$NSGC — The Discipline Token',
    'accent':         '#2ECC40',
})

# ══════════════════════════════════════════════════════════════════════════════
# CONTENT
# ══════════════════════════════════════════════════════════════════════════════
T.CHAPTERS = [
    {
        'num': '01 ——', 'title': 'Abstract',
        'blocks': [
            ('body',
             'No Sugar Coin ($NSGC) is a culture token deployed on BNB Smart Chain, built around discipline '
             'as a shared identity. It uses the symbolic language of sugar — instant gratification, impulse, '
             'and short-term thinking — as a cultural counterpoint to a community defined by structure, '
             'consistency, and long-term strength.'),
            ('body',
             '$NSGC operates as a fixed-supply, zero-tax BEP-20 token with a transparent distribution model '
             'and an open-source, verified smart contract. Its value proposition is not technical novelty. '
             'It is cultural belonging. The token exists as the on-chain representation of a tribe.'),
            ('body',
             'This document describes the philosophy, token architecture, community mechanics, and ecosystem '
             'strategy of No Sugar Coin. It makes no medical claims, no financial promises, and no guarantees '
             'of return. It describes a movement.'),
            ('quote', '"$NSGC is not trying to be useful. It is trying to be belonging."'),
        ]
    },
    {
        'num': '02 ——', 'title': 'The Problem',
        'blocks': [
            ('body',
             'Sugar is not just a food. It is the symbol of an era. Modern society has been engineered around '
             'instant gratification — notifications, algorithmic feeds, ultra-processed products, and dopamine '
             'loops designed to extract attention and spending from the weakest impulses of human behaviour. '
             'The result is a culture of short-term thinking dressed as progress.'),
            ('body',
             'Crypto, at its worst, mirrors this exactly. Projects launch with promises of instant wealth. '
             'Communities form around speculation rather than identity. Tokens disappear when the dopamine does. '
             'The cycle repeats.'),
            ('body',
             '$NSGC is built in direct opposition to this pattern — not through utility features or technical '
             'complexity, but through cultural positioning. A token that stands for the opposite of sugar: '
             'structure, patience, and delayed gratification.'),
            ('table',
             ['SUGAR REPRESENTS', '$NSGC REPRESENTS'],
             [
                 ['Instant gratification',      'Delayed gratification'],
                 ['Weak impulse control',        'Self-discipline as identity'],
                 ['Short-term dopamine',         'Long-term consistency'],
                 ['Consumption without meaning', 'Community with purpose'],
                 ['Speculation over substance',  'Culture over noise'],
             ],
             [0.5, 0.5]),
        ]
    },
    {
        'num': '03 ——', 'title': 'Vision & Philosophy',
        'blocks': [
            ('body',
             'The vision of $NSGC is to create a crypto token that functions as a cultural artifact — a signal '
             'of identity as clear and deliberate as a lifestyle brand, a gym membership, or a personal philosophy.'),
            ('body',
             'Meme tokens have proven, repeatedly, that narrative and identity drive value more reliably than '
             'utility at the community layer. $NSGC applies this principle with intention — choosing discipline '
             'as its narrative because it is enduring, universal, and genuinely aspirational.'),
            ('body',
             'The brand is built for a specific tribe: the gym community, the anti-ultra-processed movement, '
             'the 5AM crowd — people who already live by these values and now have an on-chain symbol for them.'),
            ('h3', 'Core Principles'),
            ('bullet', 'Clean Over Complex — no hidden mechanics, no confusing tokenomics. Simplicity is discipline applied to code.'),
            ('bullet', 'Culture Over Utility — identity tokens do not need to solve technical problems. They need to represent real ones.'),
            ('bullet', 'Behaviour Over Speculation — the community engine rewards consistent action, not price chasing.'),
            ('bullet', 'Tribe Over Audience — holders are participants in a movement, not spectators of a chart.'),
        ]
    },
    {
        'num': '04 ——', 'title': 'Cultural Narrative',
        'blocks': [
            ('body',
             'Every lasting movement has a clear enemy. $NSGC has sugar. Not in a literal, dietary sense. '
             'Sugar is the metaphor — the universal shorthand for everything designed to feel good immediately '
             'at the cost of what matters long-term. Ultra-processed food. Doom scrolling. Cheap dopamine. '
             'Get-rich-quick schemes. Shortcuts. Weakness dressed as convenience.'),
            ('body',
             'The $NSGC community defines itself against this. Not through preaching, not through health claims, '
             'not through moralising — but through identity. You either cut the sugar or you do not. '
             'The token is a signal of which side you are on.'),
            ('quote',
             '"We do not moralise. We do not preach. We do not make medical claims. '
             'We build a tribe of people who already chose discipline."'),
            ('h3', 'The Tribe'),
            ('body', 'The $NSGC community is not defined by demographics. It is defined by values:'),
            ('bullet', 'Consistency over motivation'),
            ('bullet', 'Structure over impulse'),
            ('bullet', 'Long-term strength over short-term comfort'),
            ('bullet', 'Discipline culture — gym, productivity, mental resilience, self-improvement'),
            ('bullet', 'Identity built on behaviour, not words'),
            ('h3', 'The Brand Voice'),
            ('body',
             'The tone of $NSGC is serious but not corporate. Minimal but not cold. Confident but not arrogant. '
             'The aesthetic draws from high-performance culture — clean lines, structured layout, sharp accents. '
             'The meme layer exists and is embraced. The philosophy beneath it is real.'),
        ]
    },
    {
        'num': '05 ——', 'title': 'Token Architecture',
        'blocks': [
            ('h3', 'Technical Specification'),
            ('speclist', [
                ('Token Name',       'No Sugar Coin'),
                ('Ticker Symbol',    '$NSGC'),
                ('Blockchain',       'BNB Smart Chain (BSC)'),
                ('Token Standard',   'BEP-20 (ERC-20 compatible)'),
                ('Total Supply',     '100,000,000 NSGC — Fixed, immutable'),
                ('Decimals',         '18'),
                ('Transfer Tax',     '0% — No buy tax. No sell tax.'),
                ('Compiler',         'Solidity v0.8.34+commit.80d5c536'),
                ('Source Code',      'Verified — BscScan Exact Match'),
                ('Base Standard',    'OpenZeppelin ERC-20 + Ownable'),
                ('Contract Address', '0x19B1b3C12642Cc08B73e6b03e52841004dc5E299'),
                ('Owner Address',    '0x1695DC0E70D012e9b4d583Bd8667323991BdaA14'),
            ]),
            ('h3', 'Token Distribution'),
            ('table',
             ['ALLOCATION', '%', 'TOKENS', 'PURPOSE'],
             [
                 ['Liquidity Pool',    '60%', '60,000,000', 'Market depth and stability'],
                 ['Community Rewards', '20%', '20,000,000', 'Discipline challenge incentives'],
                 ['Marketing',         '10%', '10,000,000', 'Growth and brand exposure'],
                 ['Team',              '5%',  '5,000,000',  'Core contributors'],
                 ['Future Burns',      '5%',  '5,000,000',  'Scarcity mechanics'],
             ],
             [0.28, 0.1, 0.22, 0.4]),
            ('h3', 'Design Philosophy'),
            ('body',
             'The token mechanics are intentionally minimal. Zero tax means zero friction — every transfer '
             'executes exactly as expected, with no hidden deductions, no reflection mechanics, and no complex '
             'logic. The contract is built on the OpenZeppelin standard, verified publicly on BscScan, and '
             'readable by anyone.'),
            ('body',
             'Clean is a feature. Complexity in token mechanics is almost always a concealment mechanism. '
             '$NSGC chooses trust through transparency.'),
        ]
    },
    {
        'num': '06 ——', 'title': 'Community Layer',
        'blocks': [
            ('body',
             'The community engine is the core of $NSGC. It transforms passive token holders into active '
             'participants through behaviour-driven reward cycles — the mechanism that creates genuine retention '
             'rather than pure speculation.'),
            ('h3', 'The 30-Day Discipline Cycle'),
            ('body',
             'Community rewards are distributed through structured 30-day challenge cycles. Each cycle has a '
             'defined theme. Participants engage by posting proof of consistency, interacting with the community, '
             'and maintaining their commitment throughout the cycle. The 20,000,000 NSGC Community Rewards Pool '
             'funds sustained engagement across these cycles.'),
            ('h3', 'Active Challenge Categories'),
            ('bullet', 'No Soda — 30 Days: zero sugar-sweetened beverages for a full cycle. Daily check-ins, memes, and community accountability.'),
            ('bullet', '30 Workouts in 30 Days: consistency over intensity. Any movement qualifies. Proof of discipline, not performance.'),
            ('bullet', '5AM Club: structured mornings as a shared identity. Early risers as a subculture. Document it, share it, own it.'),
            ('bullet', 'Ultra-Processed Detox: clean-eating culture without moralising. Self-control as a group value. No prescriptions, only proof.'),
            ('h3', 'Why Behaviour-Driven Communities Win'),
            ('bullet', 'Identity attachment forms beyond price action — holders stay through volatility'),
            ('bullet', 'Participants generate authentic, organic content that recruits new members'),
            ('bullet', 'Peer accountability creates real social bonds within the community'),
            ('bullet', 'Challenge cycles create recurring momentum rather than one-time hype events'),
            ('bullet', 'Earned rewards feel meaningful — behaviour proves commitment, not just capital'),
        ]
    },
    {
        'num': '07 ——', 'title': 'Pumpnetic Ecosystem',
        'blocks': [
            ('body',
             '$NSGC is the first cultural token within the Pumpnetic ecosystem — an internet-native '
             'infrastructure focused on decentralised projects, emerging digital communities, and on-chain identity.'),
            ('body',
             'Pumpnetic operates as the founding architecture behind $NSGC: providing direction, brand structure, '
             'technical deployment, and strategic development. The relationship between $NSGC and Pumpnetic is '
             'one of ecosystem and cultural layer — the token expresses values the broader platform is built on.'),
            ('h3', 'Ecosystem Properties'),
            ('bullet', 'Internet-native: built for decentralised, community-first environments'),
            ('bullet', 'Chain-agnostic architecture — BSC as primary deployment, expansion-ready'),
            ('bullet', 'Open-source and publicly verifiable at every layer'),
            ('bullet', 'Culture-first: projects within Pumpnetic lead with narrative, not whitepaper jargon'),
            ('bullet', 'Pseudonymous by design — identity through work and on-chain transparency'),
            ('h3', 'Official Links'),
            ('links', [
                ('Website',     'https://nsgc.pumpnetic.com'),
                ('Ecosystem',   'https://pumpnetic.com'),
                ('Telegram',    'https://t.me/NoSugarCoin'),
                ('X (Twitter)', 'https://x.com/NoSugarCoin'),
                ('Email',       'nsgc@pumpnetic.com'),
                ('GitHub',      'https://github.com/pumpneticprojects-collab/pumpnetic-public/blob/main/docs/projects/nsgc/nsgc.md'),
                ('BscScan',     'https://bscscan.com/token/0x19B1b3C12642Cc08B73e6b03e52841004dc5E299'),
            ]),
        ]
    },
    {
        'num': '08 ——', 'title': 'Governance & Founder',
        'blocks': [
            ('body',
             'No Sugar Coin is developed under the direction of NodeFounder — the pseudonymous founder and '
             'ecosystem architect behind Pumpnetic. NodeFounder is focused on internet-native infrastructure, '
             'decentralised ecosystems, and emerging digital projects.'),
            ('body',
             'Transparency is maintained through on-chain verifiability: the contract is open-source, '
             'distribution is public, and the mechanics are simple enough to require no trust beyond what '
             'the code provides.'),
            ('speclist', [
                ('Founder & Lead Architect', 'NodeFounder (Pseudonymous)'),
                ('Ecosystem',                'Pumpnetic'),
                ('Focus',                    'Internet-native infrastructure, decentralised ecosystems'),
            ]),
            ('h3', 'Governance Philosophy'),
            ('body',
             'At launch, $NSGC operates with a straightforward and honest structure: a single founding architect, '
             'an open-source and immutable contract, and a community that governs itself through participation '
             'in challenges and culture rather than formal voting mechanisms.'),
            ('body',
             'Future governance expansions — including community votes on burns, treasury decisions, and '
             'ecosystem direction — are extensions of the same principle: discipline applied collectively.'),
        ]
    },
    {
        'num': '09 ——', 'title': 'Roadmap',
        'blocks': [
            ('body',
             'The $NSGC roadmap is built around three phases of evolution. Each phase is defined by outcomes, '
             'not timelines. Progress is measured by what exists, not what is promised.'),
            ('h3', 'Phase I — Foundation'),
            ('bullet', 'Token deployment and BscScan verification'),
            ('bullet', 'Liquidity provision and LP lock'),
            ('bullet', 'Website and brand identity fully live'),
            ('bullet', 'Social channels established across X, Telegram, Discord'),
            ('bullet', 'First meme wave and community seeding'),
            ('h3', 'Phase II — The Discipline Movement'),
            ('bullet', 'First 30-day challenge cycle activation'),
            ('bullet', 'Community Rewards Pool distribution begins'),
            ('bullet', 'Micro-influencer and tribe outreach campaigns'),
            ('bullet', 'Meme competitions and coordinated community activity'),
            ('bullet', 'DEX listing and chart visibility'),
            ('h3', 'Phase III — Expansion'),
            ('bullet', 'NFT badge system — Proof of Discipline (community-voted)'),
            ('bullet', 'Limited merchandise drops tied to challenge completions'),
            ('bullet', 'Community governance on future token burns'),
            ('bullet', 'Cross-chain exploration and liquidity expansion'),
            ('bullet', 'Partnership experiments within the Pumpnetic ecosystem'),
        ]
    },
    {
        'num': '10 ——', 'title': 'Legal Disclaimer',
        'blocks': [
            ('body',
             '$NSGC is a meme and culture token. It is not a security, not an investment product, and not a '
             'financial instrument of any kind. Holding $NSGC does not confer rights, equity, dividends, or '
             'guaranteed returns of any nature.'),
            ('bullet', 'This document does not constitute financial or investment advice of any kind.'),
            ('bullet', 'No medical, dietary, or health claims are made, expressed, or implied.'),
            ('bullet', 'Past performance of similar tokens does not indicate future results.'),
            ('bullet', 'Cryptocurrency investments carry significant risk, including the total loss of capital.'),
            ('bullet', 'The token contract is provided as-is. Interact only with the verified contract address.'),
            ('bullet', '$NSGC is a cultural participation token. Engage as a community member, not as an investor.'),
            ('bullet', 'No regulatory filings have been made. This token is not registered as a security in any jurisdiction.'),
            ('space',),
            ('quote', '"Burn sugar. Mint strength."'),
        ]
    },
]

if __name__ == '__main__':
    T.build()
