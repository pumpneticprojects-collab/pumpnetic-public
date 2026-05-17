"""
================================================================================
I KNOW WHAT YOU DID COIN ($IKWYD) — WHITEPAPER BUILD SCRIPT
Pumpnetic Ecosystem · BNB Smart Chain
================================================================================
Run:  python build_ikwyd_wp.py
Requires: pumpnetic_wp_template.py in the same directory
Output: /mnt/user-data/outputs/IKWYD_WhitePaper_v1.pdf
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
    'name':           'I Know What You Did Coin',
    'ticker':         '$IKWYD',
    'tagline':        'The Blockchain Never Forgets',
    'quote':          '"Every panic sell. Every liquidation. Every rug. The blockchain remembers it all."',
    'ecosystem':      'Pumpnetic Ecosystem',

    'network':        'BNB Smart Chain',
    'supply':         '1,000,000,000',
    'tax':            '0%',
    'standard':       'BEP-20',
    'compiler':       'Solidity v0.8.34',

    'contract':       '0xA3ad36133013Db657107266c18cbe1aea0319821',
    'owner':          '0x1Ec8B2125990673E0A4C2056489482B5765C21C4',

    'website':        'https://ikwyd.pumpnetic.com',
    'ecosystem_site': 'https://pumpnetic.com',
    'bscscan':        'https://bscscan.com/token/0xA3ad36133013Db657107266c18cbe1aea0319821',
    'telegram':       'https://t.me/IKWYDCoin',
    'twitter':        'https://x.com/IKWYDCoin',
    'email':          'ikwyd@pumpnetic.com',
    'github':         'https://github.com/pumpneticprojects-collab/pumpnetic-public/blob/main/docs/projects/ikwyd/ikwyd.md',

    'output':         '/mnt/user-data/outputs/IKWYD_WhitePaper_v1.pdf',
    'author':         'NodeFounder / Pumpnetic',
    'subject':        '$IKWYD — The Blockchain Never Forgets',

    # Red/orange accent — danger, exposure, degen energy
    'accent':         '#E53E3E',
})

# ══════════════════════════════════════════════════════════════════════════════
# CONTENT
# ══════════════════════════════════════════════════════════════════════════════
T.CHAPTERS = [
    # ── 01 ────────────────────────────────────────────────────────────────────
    {
        'num': '01 ——', 'title': 'Abstract',
        'blocks': [
            ('body',
             'I Know What You Did Coin ($IKWYD) is a community token deployed on BNB Smart Chain, built '
             'around a universal truth every crypto participant shares: we have all made the trade we regret. '
             'We have all bought the top, sold the bottom, trusted the wrong project, or watched a liquidation '
             'happen in real time. The blockchain recorded every moment of it — permanently, publicly, '
             'and without mercy.'),
            ('body',
             '$IKWYD is not a meme at someone else\'s expense. It is a shared confession. A community built '
             'on radical honesty about the crypto experience — the losses, the lessons, the liquidations, '
             'and the inexplicable decision to open another trade five minutes later. This is the token for '
             'everyone who survived, and everyone still surviving.'),
            ('body',
             '$IKWYD operates as a fixed-supply, zero-tax BEP-20 token with a transparent distribution model, '
             'an open-source verified smart contract, and a community engine built on shared identity rather '
             'than price speculation. This document describes the philosophy, token architecture, community '
             'mechanics, and ecosystem strategy of I Know What You Did Coin.'),
            ('quote',
             '"We are all guilty. And now — everyone knows."'),
        ]
    },

    # ── 02 ────────────────────────────────────────────────────────────────────
    {
        'num': '02 ——', 'title': 'The Problem',
        'blocks': [
            ('body',
             'Crypto is the only market where the receipts are public. Every transaction, every wallet '
             'movement, every panic sell and every mistimed entry is permanently inscribed on a public ledger '
             'that anyone can read. Unlike traditional finance — where bad trades disappear into private '
             'brokerage statements — blockchain is transparent by design. Your history is visible. '
             'Your decisions are on record.'),
            ('body',
             'Most projects in this space treat this reality as something to ignore. They build narratives '
             'around the next win, the next pump, the next 100x. They attract communities through greed '
             'rather than truth. The result is a cycle of hype, disappointment, and exit — repeated endlessly '
             'because no one ever acknowledges what actually happened.'),
            ('body',
             '$IKWYD is built on the opposite premise. The shared experience of crypto — the losses, the '
             'regrets, the near-misses, and the hard lessons — is not something to hide. It is the most '
             'powerful community-building force in the space. Every person who has ever held a crypto wallet '
             'has a story. $IKWYD is where those stories live.'),
            ('table',
             ['CRYPTO CULTURE SAYS', '$IKWYD SAYS'],
             [
                 ['"Only show your wins"',          '"We all know about the losses"'],
                 ['"Number go up"',                 '"The chart told the truth"'],
                 ['"HODL no matter what"',          '"We saw you sell at the bottom"'],
                 ['"Early investors only"',          '"We are all degens here"'],
                 ['"This one is different"',         '"The blockchain never forgets"'],
             ],
             [0.5, 0.5]),
        ]
    },

    # ── 03 ────────────────────────────────────────────────────────────────────
    {
        'num': '03 ——', 'title': 'Vision & Philosophy',
        'blocks': [
            ('body',
             'The vision of $IKWYD is to create the community token for the entire generation of crypto '
             'participants — not just the winners, not just the early adopters, not just the whales. Everyone '
             'who has ever been in this market. Everyone who bought at the wrong time. Everyone who held '
             'too long or sold too soon. Everyone who trusted a project that disappeared. Everyone who is '
             'still here, regardless.'),
            ('body',
             'Belonging does not require a winning trade history. It requires only that you have been through '
             'the experience — and that you are honest about it. $IKWYD turns that honesty into identity, '
             'and that identity into community. This is the token that remembers what everyone else tries '
             'to forget.'),
            ('h3', 'Core Principles'),
            ('bullet',
             'Radical Honesty Over Performance — no pretending. The blockchain has the receipts and so does this community.'),
            ('bullet',
             'Shared Experience Over Exclusivity — this token belongs to everyone who has ever made a trade they regret. That is everyone.'),
            ('bullet',
             'Community Over Speculation — the value of $IKWYD is in belonging, not in price targets or promises of returns.'),
            ('bullet',
             'Humour as Healing — crypto is absurd. Laughing at our shared failures together is how this community processes and grows.'),
            ('bullet',
             'Permanence as Identity — the blockchain never forgets. Neither do we. That is the feature, not the flaw.'),
        ]
    },

    # ── 04 ────────────────────────────────────────────────────────────────────
    {
        'num': '04 ——', 'title': 'Cultural Narrative',
        'blocks': [
            ('body',
             'Every crypto participant has a story. The exact moment they bought the top. The liquidation '
             'they watched happen in slow motion. The project they believed in that turned to zero overnight. '
             'The "gem" they found early and sold at 3x — before it went to 1000x. The leverage trade that '
             'seemed rational at the time.'),
            ('body',
             'These stories are usually told quietly, in private, between people who trust each other. '
             '$IKWYD makes them public — not as mockery, but as solidarity. Because once you realise that '
             'every person in crypto has the same story, the shame dissolves. What is left is community.'),
            ('quote',
             '"Welcome to the support group. For everyone who opened another trade five minutes after '
             'their liquidation. We do not judge. We are all the same here."'),
            ('h3', 'The Confessions'),
            ('bullet',
             'Bought The Top — "This is just a dip." You bought at the exact moment before -97%. The chart was screaming. You bought anyway.'),
            ('bullet',
             'Sold The Bottom — you held through -60%, -70%, -80%... then sold at -95%. Two weeks later it 10x\'d. The blockchain has the receipts.'),
            ('bullet',
             '100x Leverage — you opened a 100x long at resistance. The candle was already red. The liquidation was instant and public.'),
            ('bullet',
             'Dev Left — "This coin is different." Forty-two seconds before the dev wallet sold everything. The audit was fake. We know.'),
            ('bullet',
             'Sold Before 1000x — you found a gem early. You were right about the project. You sold at 3x. It went to 1000x six weeks later.'),
            ('h3', 'Why This Community Works'),
            ('body',
             'Shared failure is one of the most powerful bonding forces in human psychology. Communities '
             'built around honest, mutual experience — especially experience that involves vulnerability '
             'and humour — create loyalty that price action cannot manufacture. $IKWYD does not need a '
             'bull market to be relevant. The losses are always happening. The community is always needed.'),
        ]
    },

    # ── 05 ────────────────────────────────────────────────────────────────────
    {
        'num': '05 ——', 'title': 'Token Architecture',
        'blocks': [
            ('h3', 'Technical Specification'),
            ('speclist', [
                ('Token Name',       'I Know What You Did Coin'),
                ('Ticker Symbol',    '$IKWYD'),
                ('Blockchain',       'BNB Smart Chain (BSC)'),
                ('Token Standard',   'BEP-20 (ERC-20 compatible)'),
                ('Total Supply',     '1,000,000,000 IKWYD — Fixed, immutable'),
                ('Decimals',         '18'),
                ('Transfer Tax',     '0% — No buy tax. No sell tax.'),
                ('Compiler',         'Solidity v0.8.34+commit.80d5c536'),
                ('Source Code',      'Verified — BscScan Exact Match'),
                ('Base Standard',    'OpenZeppelin ERC-20 + Ownable'),
                ('Contract Address', '0xA3ad36133013Db657107266c18cbe1aea0319821'),
                ('Owner Address',    '0x1Ec8B2125990673E0A4C2056489482B5765C21C4'),
            ]),
            ('h3', 'Token Distribution'),
            ('table',
             ['ALLOCATION', '%', 'TOKENS', 'PURPOSE'],
             [
                 ['Liquidity Pool',    '60%', '600,000,000', 'Market depth — locked'],
                 ['Community Pool',    '20%', '200,000,000', 'Meme raids, rewards, confessions'],
                 ['Marketing',         '10%', '100,000,000', 'Growth and brand exposure'],
                 ['Team',              '5%',  '50,000,000',  'Core contributors'],
                 ['Future Burns',      '5%',  '50,000,000',  'Scarcity mechanics'],
             ],
             [0.28, 0.1, 0.24, 0.38]),
            ('h3', 'Design Philosophy'),
            ('body',
             'Zero tax means zero friction. Every $IKWYD transfer executes exactly as expected — no hidden '
             'deductions, no complex reflection logic, no mechanisms designed to obscure what the contract '
             'actually does. The irony of a token about on-chain transparency having anything to hide would '
             'be too much to bear.'),
            ('body',
             'The contract is open-source, verified on BscScan, and readable by anyone. Liquidity is locked. '
             'The supply is fixed and immutable. $IKWYD practices exactly what it preaches: the blockchain '
             'never lies, and neither does this project.'),
        ]
    },

    # ── 06 ────────────────────────────────────────────────────────────────────
    {
        'num': '06 ——', 'title': 'Community Layer',
        'blocks': [
            ('body',
             'The community is the product. $IKWYD does not sell a service, a utility, or a promise of '
             'future returns. It sells belonging — to the largest, most universal group in crypto: people '
             'who have made trades they regret and kept going anyway. The community engine is designed to '
             'create recurring engagement loops that deepen identity attachment over time.'),
            ('h3', 'Meme Raids & Confession Campaigns'),
            ('body',
             'The primary community mechanic is the coordinated meme campaign — large-scale, cross-platform '
             'content drops built around the shared experiences that define crypto culture. These campaigns '
             'are not just engagement tactics. They are the mechanism by which new members recognise '
             'themselves in the content and join because they feel seen.'),
            ('bullet',
             '"We Saw Your Wallet" — coordinated raids across X and Telegram surfacing the universal crypto experiences everyone pretends did not happen.'),
            ('bullet',
             'Confession Threads — community-driven content where holders share their most legendary trades, liquidations, and rug stories without judgement.'),
            ('bullet',
             'Hall of Shame NFT Badges — community-voted on-chain recognition for the most iconic degen moments: "Bought The Top", "Sold Before 1000x", "Survived The Rug".'),
            ('bullet',
             'Wallet Confession Tool — a fun on-chain explorer that lets anyone look up their own trade history and generate a personalised $IKWYD confession card.'),
            ('h3', 'Community Rewards Pool'),
            ('body',
             'The 200,000,000 IKWYD Community Pool funds sustained engagement. Rewards flow to participants '
             'who generate the most impactful content, bring new members into the community, and contribute '
             'to the cultural layer that makes $IKWYD recognisable beyond its immediate holder base.'),
            ('h3', 'Why This Model Works'),
            ('bullet', 'The content writes itself — every person in crypto has lived these experiences'),
            ('bullet', 'Humour creates virality — the memes are relatable to anyone who has ever held a token'),
            ('bullet', 'No bull market required — losses are always happening, the community is always relevant'),
            ('bullet', 'Emotional resonance drives retention — people stay where they feel understood'),
            ('bullet', 'The community grows every time the market crashes — the worst days become the best content'),
        ]
    },

    # ── 07 ────────────────────────────────────────────────────────────────────
    {
        'num': '07 ——', 'title': 'Pumpnetic Ecosystem',
        'blocks': [
            ('body',
             '$IKWYD is an official project within the Pumpnetic ecosystem — an internet-native infrastructure '
             'focused on decentralised projects, emerging digital communities, and on-chain identity. '
             '$IKWYD represents the community and culture layer of the ecosystem: the token that speaks '
             'to the universal crypto experience and brings people in through recognition rather than hype.'),
            ('body',
             'Pumpnetic provides the founding architecture behind $IKWYD: direction, brand structure, '
             'technical deployment, and strategic development. Projects within the ecosystem are designed '
             'to cross-promote, share audience, and build a broader community network over time.'),
            ('h3', 'Ecosystem Properties'),
            ('bullet', 'Internet-native: built for decentralised, community-first environments'),
            ('bullet', 'Chain-agnostic architecture — BSC as primary deployment, expansion-ready'),
            ('bullet', 'Open-source and publicly verifiable at every layer'),
            ('bullet', 'Culture-first: every Pumpnetic project leads with narrative and identity'),
            ('bullet', 'Pseudonymous by design — identity through work and on-chain transparency'),
            ('h3', 'Official Links'),
            ('links', [
                ('Website',     'https://ikwyd.pumpnetic.com'),
                ('Ecosystem',   'https://pumpnetic.com'),
                ('Telegram',    'https://t.me/IKWYDCoin'),
                ('X (Twitter)', 'https://x.com/IKWYDCoin'),
                ('Email',       'ikwyd@pumpnetic.com'),
                ('GitHub',      'https://github.com/pumpneticprojects-collab/pumpnetic-public/blob/main/docs/projects/ikwyd/ikwyd.md'),
                ('BscScan',     'https://bscscan.com/token/0xA3ad36133013Db657107266c18cbe1aea0319821'),
            ]),
        ]
    },

    # ── 08 ────────────────────────────────────────────────────────────────────
    {
        'num': '08 ——', 'title': 'Governance & Founder',
        'blocks': [
            ('body',
             'I Know What You Did Coin is developed under the direction of NodeFounder — the pseudonymous '
             'founder and ecosystem architect behind Pumpnetic. NodeFounder is focused on internet-native '
             'infrastructure, decentralised ecosystems, and emerging digital projects.'),
            ('body',
             'The project operates under a pseudonymous identity consistent with the broader ethos of '
             'decentralised, community-first crypto culture. Transparency is maintained through on-chain '
             'verifiability: the contract is open-source, distribution is public, and every mechanic is '
             'simple enough to require no trust beyond what the code provides. Fitting, for a project '
             'built on the premise that the blockchain always tells the truth.'),
            ('speclist', [
                ('Founder & Lead Architect', 'NodeFounder (Pseudonymous)'),
                ('Ecosystem',                'Pumpnetic'),
                ('Focus',                    'Internet-native infrastructure, decentralised ecosystems'),
            ]),
            ('h3', 'Governance Philosophy'),
            ('body',
             'At launch, $IKWYD operates with a clear and honest structure: a single founding architect, '
             'an immutable open-source contract, and a community that governs itself through participation '
             'in culture, meme campaigns, and confession threads rather than formal voting mechanisms.'),
            ('body',
             'Future governance expansions — community votes on token burns, treasury allocation, Hall of '
             'Shame nominations, and ecosystem direction — will be introduced as the community matures. '
             'All governance will be public, on-chain where possible, and consistent with the core principle '
             'of $IKWYD: no hiding, no pretending, no obscuring the truth.'),
        ]
    },

    # ── 09 ────────────────────────────────────────────────────────────────────
    {
        'num': '09 ——', 'title': 'Roadmap',
        'blocks': [
            ('body',
             'The $IKWYD roadmap is defined by outcomes, not promises. Each phase is measured by what '
             'exists and what the community has built — not by what was announced on a slide deck.'),
            ('h3', 'Phase I — The Confession'),
            ('bullet', 'Token deployment on BNB Smart Chain and BscScan verification'),
            ('bullet', 'Liquidity added and locked — on-chain and transparent'),
            ('bullet', 'Website live — the blockchain outs itself'),
            ('bullet', 'Telegram and X communities launched'),
            ('bullet', 'Pumpnetic ecosystem listing'),
            ('h3', 'Phase II — The Exposure'),
            ('bullet', 'Meme campaign: "We Saw Your Wallet" — coordinated cross-platform launch'),
            ('bullet', 'Viral meme drops across X and Telegram'),
            ('bullet', 'Community raids and degen onboarding'),
            ('bullet', 'Micro-influencer and crypto Twitter push'),
            ('bullet', 'Pumpnetic ecosystem cross-promotion'),
            ('h3', 'Phase III — The Hall of Shame'),
            ('bullet', 'DEX listing confirmed'),
            ('bullet', 'Hall of Shame NFT badges for degens — community voted'),
            ('bullet', 'Community voting and meme-driven token burns'),
            ('bullet', 'Merch drops — "Paper Hands" collection'),
            ('bullet', 'Wallet confession tool — fun on-chain trade history explorer'),
            ('h3', 'Phase IV — The Reckoning'),
            ('bullet', 'CMC and CoinGecko listing applications'),
            ('bullet', 'Larger meme and culture campaigns — broader crypto audience'),
            ('bullet', 'Partnership announcements within and beyond Pumpnetic'),
            ('bullet', 'Cross-community raids with aligned projects'),
            ('bullet', 'The meme coin that remembered everything — worldwide recognition'),
        ]
    },

    # ── 10 ────────────────────────────────────────────────────────────────────
    {
        'num': '10 ——', 'title': 'Legal Disclaimer',
        'blocks': [
            ('body',
             '$IKWYD is a meme and community culture token. It is not a security, not an investment product, '
             'and not a financial instrument of any kind. Holding $IKWYD does not confer rights, equity, '
             'dividends, or guaranteed returns of any nature.'),
            ('bullet', 'This document does not constitute financial or investment advice of any kind.'),
            ('bullet', 'No financial returns are promised, implied, or guaranteed.'),
            ('bullet', 'Cryptocurrency is highly speculative and volatile. You may lose all funds.'),
            ('bullet', 'Past performance of similar tokens does not indicate future results.'),
            ('bullet', 'The token contract is provided as-is. Interact only with the verified contract address.'),
            ('bullet', '$IKWYD is a cultural participation token. Engage as a community member, not as an investor.'),
            ('bullet', 'No regulatory filings have been made. This token is not registered as a security in any jurisdiction.'),
            ('bullet', 'Do your own research. Never invest more than you can afford to lose.'),
            ('space',),
            ('quote',
             '"The blockchain never forgets. Neither do we. — But we are all in this together."'),
        ]
    },
]

if __name__ == '__main__':
    T.build()
