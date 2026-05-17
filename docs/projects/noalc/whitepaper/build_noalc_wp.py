"""
================================================================================
NO ALCOHOL COIN ($NOALC) — WHITEPAPER BUILD SCRIPT
Pumpnetic Ecosystem · BNB Smart Chain
================================================================================
Run:  python build_noalc_wp.py
Requires: pumpnetic_wp_template.py in the same directory
Output: /mnt/user-data/outputs/NOALC_WhitePaper_v1.pdf
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
    'name':           'No Alcohol Coin',
    'ticker':         '$NOALC',
    'tagline':        'Raise Yourself',
    'quote':          '"You don\'t need alcohol to elevate the moment. Elevation doesn\'t require alteration."',
    'ecosystem':      'Pumpnetic Ecosystem',

    'network':        'BNB Smart Chain',
    'supply':         '1,000,000,000',
    'tax':            '0%',
    'standard':       'BEP-20',
    'compiler':       'Solidity v0.8.34',

    'contract':       '0xa223dC6241Ab785b3EA81318B098E06BD6527158',
    'owner':          '0x114605a7EcE35716Bea9173C5959ba02B2f666e0',

    'website':        'https://noalc.pumpnetic.com',
    'ecosystem_site': 'https://pumpnetic.com',
    'bscscan':        'https://bscscan.com/token/0xa223dC6241Ab785b3EA81318B098E06BD6527158',
    'telegram':       'https://t.me/NOALCcoin',
    'twitter':        'https://x.com/NoalcCoin',
    'email':          'noalc@pumpnetic.com',
    'github':         'https://github.com/pumpneticprojects-collab/pumpnetic-public/blob/main/docs/projects/noalc/noalc.md',

    'output':         '/mnt/user-data/outputs/NOALC_WhitePaper_v1.pdf',
    'author':         'NodeFounder / Pumpnetic',
    'subject':        '$NOALC — Raise Yourself',

    # Teal/emerald — clarity, freshness, elevation, clean energy
    'accent':         '#0D9488',
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
             'No Alcohol Coin ($NOALC) is a clarity-first community token deployed on BNB Smart Chain, '
             'built around a cultural movement that is already happening: a generation choosing presence '
             'over fogginess, real confidence over liquid courage, and better mornings over regret. '
             '$NOALC gives this movement its on-chain identity — a shared symbol for everyone who chooses '
             'to raise themselves.'),
            ('body',
             'This is not a prohibition movement. This is not a moral argument. $NOALC makes no medical '
             'claims, no health guarantees, and no judgements about how others choose to live. It is a '
             'cultural token for a specific tribe: people who understand that clarity compounds, that every '
             'choice adds up, and that the best version of themselves does not require alteration to show up.'),
            ('body',
             '$NOALC operates as a fixed-supply, zero-tax BEP-20 token with a transparent distribution '
             'model, an open-source verified smart contract, and a community engine built on shared '
             'identity and lifestyle accountability. This document describes the philosophy, token '
             'architecture, community mechanics, and ecosystem strategy of No Alcohol Coin.'),
            ('quote',
             '"We elevate the moment by elevating ourselves."'),
        ]
    },

    # ── 02 ────────────────────────────────────────────────────────────────────
    {
        'num': '02 ——', 'title': 'The Problem',
        'blocks': [
            ('body',
             'Alcohol has been normalised as the default setting for celebration, confidence, stress '
             'relief, and social connection. This normalisation is so deep that choosing not to drink '
             'in social situations is still treated as the exception — as something that requires '
             'explanation. The question is always "why aren\'t you drinking?" rather than "why are you?"'),
            ('body',
             'That normalisation comes with a hidden tax. Foggy decisions. Reduced performance the '
             'following day. Emotional volatility. Momentum lost to recovery. Money spent on something '
             'that actively degrades the very qualities — sharpness, presence, confidence — it claims '
             'to provide. The trade is almost always worse than it appears in the moment.'),
            ('body',
             'At the same time, a real cultural shift is already underway. The sober-curious movement, '
             'the rise of alcohol-free alternatives, the growing mainstream acceptance of not drinking — '
             'these are not fringe phenomena. They represent a generation quietly choosing differently. '
             '$NOALC gives that choice a community, an identity, and an on-chain home.'),
            ('table',
             ['THE DEFAULT SETTING', 'THE $NOALC CHOICE'],
             [
                 ['Alcohol as social default',        'Presence as the standard'],
                 ['Confidence through intoxication',  'Confidence built from within'],
                 ['Foggy mornings as the norm',       'Every morning as a win'],
                 ['Energy that crashes',              'Natural energy that compounds'],
                 ['Identity through consumption',     'Identity through elevation'],
                 ['Social pressure to participate',   'Community that lifts instead'],
             ],
             [0.5, 0.5]),
        ]
    },

    # ── 03 ────────────────────────────────────────────────────────────────────
    {
        'num': '03 ——', 'title': 'Vision & Philosophy',
        'blocks': [
            ('body',
             'The vision of $NOALC is to create the on-chain symbol for a clarity-first lifestyle — '
             'a cultural token that functions as a signal of identity as clear and deliberate as a '
             'lifestyle brand, a training discipline, or a personal standard. Not for everyone. '
             'For the people who already understand what they are choosing and why.'),
            ('body',
             'The movement is broader than crypto. It exists in gyms, in morning routines, in the '
             'growing community of people who have quietly decided that they perform better, connect '
             'more genuinely, and live more fully without alcohol as a constant. $NOALC gives that '
             'community a shared token, a shared vocabulary, and a shared space on-chain.'),
            ('h3', 'Core Principles'),
            ('bullet',
             'Elevation Over Alteration — the best version of you does not require a substance to show up. Clarity is the starting point, not the reward.'),
            ('bullet',
             'Identity, Not Restriction — $NOALC is not about what you are giving up. It is about who you are becoming. This distinction is everything.'),
            ('bullet',
             'No Judgement, No Preaching — this community does not moralise. It does not lecture. It simply represents a choice and holds space for everyone making it.'),
            ('bullet',
             'Clarity Compounds — every sharp conversation, every clear decision, every better morning adds up. The lifestyle is the edge.'),
            ('bullet',
             'Community That Lifts — belonging to something that raises the standard is itself a form of elevation. This community exists to make the choice feel powerful.'),
        ]
    },

    # ── 04 ────────────────────────────────────────────────────────────────────
    {
        'num': '04 ——', 'title': 'Cultural Narrative',
        'blocks': [
            ('body',
             'NØALC is a brand and a posture. The crossed-out letter is deliberate — not aggressive, '
             'not preachy, just clear. A quiet signal that means something specific to the people '
             'who recognise it. Like a lifestyle brand that does not need to explain itself to its tribe.'),
            ('body',
             'The movement is built on a simple premise: real elevation — in conversation, in '
             'performance, in presence, in confidence — comes from within. It comes from movement, '
             'music, purpose, and people. It comes from the discipline of showing up consistently '
             'as your clearest self. Alcohol is not the enemy. It is simply unnecessary for what '
             'this community is building.'),
            ('quote',
             '"This is not about what you\'re giving up. It\'s about who you\'re becoming. '
             'Connection without distortion. Celebration without self-sabotage."'),
            ('h3', 'The Clarity Pillars'),
            ('bullet',
             'Natural Energy — real elevation comes from movement, music, purpose, and people. Your energy is already there. You just choose it.'),
            ('bullet',
             'Clear Decisions — clarity compounds. Every conversation, every opportunity — engaged fully present, with a sharp mind and stronger outcomes.'),
            ('bullet',
             'Better Mornings — standards create momentum. Wake up ahead. Every single day is a morning where you are already winning.'),
            ('bullet',
             'Real Confidence — built from discipline, from consistency, from showing up as yourself. Not poured. Not borrowed. Earned.'),
            ('bullet',
             'Stronger Together — a community that holds each other accountable, makes clarity look powerful, and makes the choice feel like the obvious one.'),
            ('h3', 'Who This Is For'),
            ('body',
             'The $NOALC community is not defined by abstinence as a label. It is defined by the '
             'choice to prioritise clarity — however that looks in practice. The tribe includes '
             'anyone who has ever chosen a clear mind over a blurred one and felt better for it. '
             'Anyone who has woken up without a hangover and understood what they had been trading '
             'away. Anyone who simply values what they can do when they are fully present. '
             'Your choice to show up clear is your membership card.'),
        ]
    },

    # ── 05 ────────────────────────────────────────────────────────────────────
    {
        'num': '05 ——', 'title': 'Token Architecture',
        'blocks': [
            ('h3', 'Technical Specification'),
            ('speclist', [
                ('Token Name',       'No Alcohol Coin'),
                ('Ticker Symbol',    '$NOALC'),
                ('Blockchain',       'BNB Smart Chain (BSC)'),
                ('Token Standard',   'BEP-20 (ERC-20 compatible)'),
                ('Total Supply',     '1,000,000,000 NOALC — Fixed, immutable'),
                ('Decimals',         '18'),
                ('Transfer Tax',     '0% — No buy tax. No sell tax.'),
                ('Compiler',         'Solidity v0.8.34+commit.80d5c536'),
                ('Source Code',      'Verified — BscScan Exact Match'),
                ('Base Standard',    'OpenZeppelin ERC-20 + Ownable'),
                ('Contract Address', '0xa223dC6241Ab785b3EA81318B098E06BD6527158'),
                ('Owner Address',    '0x114605a7EcE35716Bea9173C5959ba02B2f666e0'),
            ]),
            ('h3', 'Token Distribution'),
            ('table',
             ['ALLOCATION', '%', 'TOKENS', 'PURPOSE'],
             [
                 ['Liquidity Pool',    '60%', '600,000,000', 'Market depth — locked'],
                 ['Community Pool',    '20%', '200,000,000', 'Clarity challenges and rewards'],
                 ['Marketing',         '10%', '100,000,000', 'Growth and brand exposure'],
                 ['Team',              '5%',  '50,000,000',  'Core contributors'],
                 ['Future Burns',      '5%',  '50,000,000',  'Scarcity mechanics'],
             ],
             [0.28, 0.1, 0.24, 0.38]),
            ('h3', 'Design Philosophy'),
            ('body',
             'Zero tax means zero friction — completely aligned with the clarity-first philosophy. '
             'Every $NOALC transfer executes exactly as expected: no hidden deductions, no reflection '
             'mechanics, no complexity that obscures what the token actually does. A project built '
             'around transparency and clear choices should have a contract that reflects those values.'),
            ('body',
             'The contract is built on the OpenZeppelin standard, verified publicly on BscScan, and '
             'readable by anyone. Liquidity is locked. The supply is fixed and immutable. '
             'Clean mechanics are a feature — just like clarity itself.'),
        ]
    },

    # ── 06 ────────────────────────────────────────────────────────────────────
    {
        'num': '06 ——', 'title': 'Community Layer',
        'blocks': [
            ('body',
             'The community is what makes $NOALC real. The token is the on-chain symbol. The community '
             'is the movement. The two are inseparable — because a clarity-first lifestyle without '
             'people to share it with is just a personal choice, and a token without a genuine '
             'community behind it is just a contract address. $NOALC is built to be both at once.'),
            ('h3', '30-Day Clarity Challenges'),
            ('body',
             'The primary community mechanic is the structured challenge cycle — 30-day commitment '
             'periods built around specific clarity goals. Participants post daily check-ins, hold '
             'each other accountable, share experiences, and document the real impact of the choice '
             'they are making. The 200,000,000 NOALC Community Pool funds rewards across these cycles.'),
            ('bullet',
             'Dry 30 — thirty days completely clear. Daily check-ins, community accountability, honest reflections on what changes.'),
            ('bullet',
             'Sober Social — thirty days of fully present social engagement. Events, conversations, and connections without alteration.'),
            ('bullet',
             'Clarity Streak — ongoing personal commitment tracking. Community leaderboard, shareable badges, peer recognition.'),
            ('bullet',
             'Better Mornings Challenge — commit to waking up clear every day for thirty days. Track the compound effect over time.'),
            ('h3', 'Community Mechanics'),
            ('bullet',
             'Clarity Badges — shareable on-chain recognition for challenge completions: "30 Days Clear", "Sober Social", "Better Mornings".'),
            ('bullet',
             'Creator Collabs — partnerships with lifestyle creators, wellness voices, and sober-curious communities across X and beyond.'),
            ('bullet',
             'Meme Campaign: "Raise Yourself" — coordinated content drops that make the clarity choice feel aspirational and powerful.'),
            ('bullet',
             'Community Meetups — real-world events where the NØALC identity becomes tangible. The on-chain community meets in person.'),
            ('bullet',
             'NØALC Merch — wear the identity. Drops tied to challenge completions and community milestones.'),
            ('h3', 'Why Lifestyle-Driven Communities Win'),
            ('bullet', 'Identity attachment goes far deeper than price action — the lifestyle is the reason to stay'),
            ('bullet', 'Challenge cycles create recurring engagement and organic content without manufactured hype'),
            ('bullet', 'Real-world relevance means the community is never purely dependent on market conditions'),
            ('bullet', 'Accountability loops create genuine relationships — not just token holders, but people'),
            ('bullet', 'The movement is already happening — $NOALC is joining something real, not inventing it'),
        ]
    },

    # ── 07 ────────────────────────────────────────────────────────────────────
    {
        'num': '07 ——', 'title': 'Pumpnetic Ecosystem',
        'blocks': [
            ('body',
             '$NOALC is an official project within the Pumpnetic ecosystem — an internet-native '
             'infrastructure focused on decentralised projects, emerging digital communities, and '
             'on-chain identity. Within the ecosystem, $NOALC represents the clarity and lifestyle '
             'layer: the token that connects on-chain culture to real-world values and real-world change.'),
            ('body',
             'Pumpnetic provides the founding architecture behind $NOALC: direction, brand structure, '
             'technical deployment, and strategic development. Projects within the ecosystem are '
             'designed to cross-promote, share audience, and build a broader community network — '
             'each with its own distinct identity and cultural layer. Clarity compounds. So does community.'),
            ('h3', 'Ecosystem Properties'),
            ('bullet', 'Internet-native: built for decentralised, community-first environments'),
            ('bullet', 'Chain-agnostic architecture — BSC as primary deployment, expansion-ready'),
            ('bullet', 'Open-source and publicly verifiable at every layer'),
            ('bullet', 'Culture-first: every Pumpnetic project leads with narrative and identity'),
            ('bullet', 'Pseudonymous by design — identity through work and on-chain transparency'),
            ('h3', 'Official Links'),
            ('links', [
                ('Website',     'https://noalc.pumpnetic.com'),
                ('Ecosystem',   'https://pumpnetic.com'),
                ('Telegram',    'https://t.me/NOALCcoin'),
                ('X (Twitter)', 'https://x.com/NoalcCoin'),
                ('Email',       'noalc@pumpnetic.com'),
                ('GitHub',      'https://github.com/pumpneticprojects-collab/pumpnetic-public/blob/main/docs/projects/noalc/noalc.md'),
                ('BscScan',     'https://bscscan.com/token/0xa223dC6241Ab785b3EA81318B098E06BD6527158'),
            ]),
        ]
    },

    # ── 08 ────────────────────────────────────────────────────────────────────
    {
        'num': '08 ——', 'title': 'Governance & Founder',
        'blocks': [
            ('body',
             'No Alcohol Coin is developed under the direction of NodeFounder — the pseudonymous founder '
             'and ecosystem architect behind Pumpnetic. NodeFounder is focused on internet-native '
             'infrastructure, decentralised ecosystems, and emerging digital projects built around '
             'genuine cultural identity.'),
            ('body',
             'The project operates under a pseudonymous identity consistent with the ethos of '
             'decentralised, community-first crypto culture. Transparency is maintained through '
             'on-chain verifiability: the contract is open-source, distribution is public, '
             'and the mechanics are simple enough to require no trust beyond what the code provides.'),
            ('speclist', [
                ('Founder & Lead Architect', 'NodeFounder (Pseudonymous)'),
                ('Ecosystem',                'Pumpnetic'),
                ('Focus',                    'Internet-native infrastructure, decentralised ecosystems'),
            ]),
            ('h3', 'Governance Philosophy'),
            ('body',
             'At launch, $NOALC operates with a clear and honest structure: a single founding architect, '
             'an immutable open-source contract, and a community that governs itself through participation '
             'in challenges, lifestyle accountability, and cultural content rather than formal voting.'),
            ('body',
             'Future governance expansions — community votes on challenge structures, token burns, '
             'merch drops, ecosystem partnerships, and treasury direction — will be introduced as '
             'the community grows. All governance will be consistent with the core principle of '
             '$NOALC: clear, honest, and fully present.'),
        ]
    },

    # ── 09 ────────────────────────────────────────────────────────────────────
    {
        'num': '09 ——', 'title': 'Roadmap',
        'blocks': [
            ('body',
             'The $NOALC roadmap is defined by outcomes, not timelines. Each phase is measured by '
             'what exists and what the community has built — not by what was announced on a slide deck. '
             'Culture first. Community second. Real-world impact third.'),
            ('h3', 'Phase I — The Movement Begins'),
            ('bullet', 'Token deployment on BNB Smart Chain and BscScan verification'),
            ('bullet', 'Liquidity added and locked — on-chain and transparent'),
            ('bullet', 'Website live — the clarity era starts here'),
            ('bullet', 'Telegram and X communities launched'),
            ('bullet', 'Pumpnetic ecosystem listing'),
            ('h3', 'Phase II — Culture Goes Viral'),
            ('bullet', 'Meme campaign: "Raise Yourself" — coordinated cross-platform launch'),
            ('bullet', '30-day clarity streak challenges — first cycle activates'),
            ('bullet', 'Community raids and creator collabs across X and Telegram'),
            ('bullet', 'Shareable clarity badges and accountability loops go live'),
            ('bullet', 'Pumpnetic ecosystem cross-promotion'),
            ('h3', 'Phase III — Merch & Real World'),
            ('bullet', 'DEX listing confirmed'),
            ('bullet', 'NØALC merch drop — wear the identity'),
            ('bullet', 'Community meetups and clarity-first social events'),
            ('bullet', 'Influencer and lifestyle creator partnerships'),
            ('bullet', 'Clarity challenge leaderboard and community rewards'),
            ('h3', 'Phase IV — The New Era'),
            ('bullet', 'CMC and CoinGecko listing applications'),
            ('bullet', 'Brand partnerships in wellness and lifestyle sectors'),
            ('bullet', 'Cross-community expansion beyond crypto'),
            ('bullet', 'Global movement — NØALC worldwide'),
            ('bullet', 'The token that raised a generation'),
        ]
    },

    # ── 10 ────────────────────────────────────────────────────────────────────
    {
        'num': '10 ——', 'title': 'Legal Disclaimer',
        'blocks': [
            ('body',
             '$NOALC is a meme and community culture token. It is not a security, not an investment '
             'product, and not a financial instrument of any kind. Holding $NOALC does not confer '
             'rights, equity, dividends, or guaranteed returns of any nature.'),
            ('bullet', 'This document does not constitute financial or investment advice of any kind.'),
            ('bullet', 'No medical, dietary, or health claims are made, expressed, or implied.'),
            ('bullet', '$NOALC does not promote, prescribe, or guarantee any health outcomes.'),
            ('bullet', 'Cryptocurrency is highly speculative and volatile. You may lose all funds invested.'),
            ('bullet', 'Past performance of similar tokens does not indicate future results.'),
            ('bullet', 'The token contract is provided as-is. Interact only with the verified contract address.'),
            ('bullet', '$NOALC is a cultural participation token. Engage as a community member, not as an investor.'),
            ('bullet', 'No regulatory filings have been made. This token is not registered as a security in any jurisdiction.'),
            ('bullet', 'Do your own research. Never invest more than you can afford to lose.'),
            ('space',),
            ('quote',
             '"Raise yourself. The new era starts here. 🍀"'),
        ]
    },
]

if __name__ == '__main__':
    T.build()
