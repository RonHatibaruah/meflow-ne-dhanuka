import re

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MediFlow-NE | AI Medicine Demand Forecasting & Multi-Echelon Replenishment Platform</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <!-- Leaflet Map CSS & JS -->
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&display=swap');
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #f8fafc; color: #0f172a; }
        .hero-gradient { background: radial-gradient(120% 120% at 50% 0%, #eff6ff 0%, #f8fafc 100%); }
        .card-base { background: #ffffff; border: 1px solid #e2e8f0; box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px -1px rgba(0, 0, 0, 0.05); }
        .card-elevated { background: #ffffff; border: 1px solid #cbd5e1; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.06), 0 4px 6px -4px rgba(0, 0, 0, 0.05); }
        #supplyMap { height: 440px; width: 100%; border-radius: 0.75rem; z-index: 10; }
        .pulse-emerald { animation: pulseGreen 2s infinite; }
        @keyframes pulseGreen { 0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.5); } 70% { box-shadow: 0 0 0 8px rgba(16, 185, 129, 0); } 100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); } }
    </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-50 text-slate-900">

    <!-- Top Navigation Header -->
    <header class="bg-white/95 backdrop-blur-md border-b border-slate-200 sticky top-0 z-50 px-6 py-3.5 flex flex-wrap items-center justify-between gap-4 shadow-sm">
        <div class="flex items-center space-x-3.5">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-blue-700 via-indigo-600 to-cyan-500 flex items-center justify-center shadow-md shadow-blue-500/20 text-white">
                <i data-lucide="activity" class="w-6 h-6"></i>
            </div>
            <div>
                <div class="flex items-center space-x-2">
                    <span class="text-xl font-extrabold tracking-tight text-slate-900">
                        MediFlow<span class="text-blue-600">-NE</span>
                    </span>
                    <span class="text-xs px-2.5 py-0.5 rounded-full bg-blue-50 border border-blue-200 text-blue-700 font-bold">
                        NESFIC-I-09
                    </span>
                    <span class="text-xs px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-medium hidden sm:inline-block">
                        G.R. Dhanuka Group
                    </span>
                </div>
                <p class="text-xs text-slate-500 font-medium">AI Medicine Demand Forecasting & Multi-Echelon Inventory Platform for Northeast India</p>
            </div>
        </div>

        <!-- Header Actions -->
        <div class="flex items-center space-x-2.5 flex-wrap">
            <button onclick="scrollToSection('landingSection')" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 text-xs font-semibold transition">
                Overview
            </button>
            <button onclick="scrollToSection('radarSection')" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 text-xs font-semibold transition">
                GIS Radar
            </button>
            <button onclick="scrollToSection('forecastSection')" class="px-3 py-1.5 rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 text-xs font-semibold transition">
                AI Forecast
            </button>
            <button onclick="openTutorialModal()" class="px-3.5 py-1.5 rounded-lg bg-amber-50 hover:bg-amber-100 text-amber-800 border border-amber-300 text-xs font-semibold flex items-center space-x-1.5 transition">
                <i data-lucide="help-circle" class="w-3.5 h-3.5 text-amber-600"></i>
                <span>Tutorial & Guide</span>
            </button>
            <button id="adminLoginHeaderBtn" onclick="openAdminModal()" class="px-3.5 py-1.5 rounded-lg bg-purple-50 hover:bg-purple-100 text-purple-800 border border-purple-300 text-xs font-semibold flex items-center space-x-1.5 transition">
                <i data-lucide="lock" class="w-3.5 h-3.5 text-purple-600"></i>
                <span id="adminHeaderLabel">Admin Console (Login)</span>
            </button>
            <a href="NESFIC_I_09_Dhanuka_Proposal_PoW.pdf" target="_blank" class="px-3.5 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white text-xs font-semibold flex items-center space-x-1.5 shadow-sm transition">
                <i data-lucide="download" class="w-3.5 h-3.5"></i>
                <span>Proposal PDF (15 Pages)</span>
            </a>
        </div>
    </header>

    <!-- Main Content Container -->
    <main class="flex-1 space-y-10">

        <!-- LANDING PAGE HERO SECTION -->
        <section id="landingSection" class="hero-gradient border-b border-slate-200 py-12 px-6">
            <div class="max-w-7xl mx-auto space-y-8">
                
                <!-- Tagline & Challenge Badge -->
                <div class="flex flex-wrap items-center justify-between gap-3">
                    <div class="inline-flex items-center space-x-2 bg-white px-3.5 py-1.5 rounded-full border border-slate-200 shadow-sm text-xs">
                        <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 pulse-emerald"></span>
                        <span class="font-bold text-slate-800">North East Seva First Innovation Challenge (NESFIC 2026)</span>
                        <span class="text-slate-400">|</span>
                        <span class="text-blue-600 font-semibold">Assam Startup Foundation</span>
                    </div>
                    <div class="text-xs text-slate-600">
                        Total Grant: <strong class="text-slate-900 font-bold">₹40.00 Lakhs</strong> · Technical Team: <strong class="text-blue-700 font-bold">₹20.00 Lakhs (50%)</strong>
                    </div>
                </div>

                <!-- Main Hero Pitch -->
                <div class="grid grid-cols-1 lg:grid-cols-12 gap-8 items-center">
                    <div class="lg:col-span-8 space-y-4">
                        <h1 class="text-3xl md:text-4xl font-extrabold text-slate-900 tracking-tight leading-tight">
                            Predictive Medicine Availability Across Northeast India's Challenging Terrains
                        </h1>
                        <p class="text-base text-slate-600 leading-relaxed max-w-3xl">
                            Engineered specifically for <strong class="text-slate-900">G.R. Dhanuka Group’s</strong> multi-state pharmaceutical distribution network. 
                            <strong>MediFlow-NE</strong> overcomes seasonal Brahmaputra floods, transit washouts along NH-6/NH-29, and fragmented billing ledgers using 
                            <strong class="text-blue-700">Temporal Fusion Transformers (TFT)</strong> and <strong class="text-emerald-700">Multi-Echelon Pre-Positioning (MEIO)</strong>.
                        </p>

                        <!-- Key Value Props -->
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-3 pt-2">
                            <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-sm">
                                <div class="text-xs text-slate-500 font-medium">Prevent Stockouts</div>
                                <div class="text-lg font-bold text-blue-700">65% Reduction</div>
                                <div class="text-[11px] text-slate-500">In anti-snake venom, insulin & vital drugs</div>
                            </div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-sm">
                                <div class="text-xs text-slate-500 font-medium">Forecast Accuracy</div>
                                <div class="text-lg font-bold text-emerald-700">11.2% MAPE</div>
                                <div class="text-[11px] text-slate-500">Down from 36.5% traditional heuristic error</div>
                            </div>
                            <div class="p-3 bg-white rounded-xl border border-slate-200 shadow-sm">
                                <div class="text-xs text-slate-500 font-medium">Expiry Arbitrage</div>
                                <div class="text-lg font-bold text-purple-700">45% Less Scrap</div>
                                <div class="text-[11px] text-slate-500">FEFO cross-tier rebalancing to hospitals</div>
                            </div>
                        </div>

                        <!-- Hero CTAs -->
                        <div class="flex items-center space-x-3 pt-2 flex-wrap gap-2">
                            <button onclick="scrollToSection('radarSection')" class="px-5 py-2.5 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs shadow-md shadow-blue-600/20 flex items-center gap-2 transition">
                                <i data-lucide="play" class="w-4 h-4"></i>
                                <span>Explore Interactive Live Simulator</span>
                            </button>
                            <button onclick="openAdminModal()" class="px-4 py-2.5 rounded-xl bg-white hover:bg-slate-100 text-slate-800 border border-slate-300 font-bold text-xs shadow-sm flex items-center gap-2 transition">
                                <i data-lucide="shield-check" class="w-4 h-4 text-purple-600"></i>
                                <span>Launch Admin Command Console</span>
                            </button>
                            <a href="https://github.com/RonHatibaruah/meflow-ne-dhanuka" target="_blank" class="px-4 py-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-semibold text-xs shadow-sm flex items-center gap-2 transition">
                                <i data-lucide="github" class="w-4 h-4"></i>
                                <span>GitHub Repository</span>
                            </a>
                        </div>
                    </div>

                    <!-- Right Card: Problem to Solution Impact -->
                    <div class="lg:col-span-4 bg-white p-5 rounded-2xl border border-slate-200 shadow-md space-y-4">
                        <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
                            <h2 class="text-xs font-bold text-slate-900 uppercase tracking-wider flex items-center gap-1.5">
                                <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600"></i>
                                <span>Solution Pillars</span>
                            </h2>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-bold">12-Month Plan</span>
                        </div>

                        <div class="space-y-3 text-xs">
                            <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200/80 space-y-1">
                                <div class="font-bold text-slate-900 flex items-center gap-1.5">
                                    <span class="w-4 h-4 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-[10px]">1</span>
                                    Geospatial Hazard Integration
                                </div>
                                <p class="text-slate-600 text-[11px]">Real-time IMD precipitation + Central Water Commission river levels trigger automatic pre-positioning before road washouts.</p>
                            </div>

                            <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200/80 space-y-1">
                                <div class="font-bold text-slate-900 flex items-center gap-1.5">
                                    <span class="w-4 h-4 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-[10px]">2</span>
                                    Non-Invasive ERP Ingestion
                                </div>
                                <p class="text-slate-600 text-[11px]">Syncs directly with existing Marg ERP, Tally Prime, and Busy setups without forcing stockists to change their billing software.</p>
                            </div>

                            <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200/80 space-y-1">
                                <div class="font-bold text-slate-900 flex items-center gap-1.5">
                                    <span class="w-4 h-4 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-[10px]">3</span>
                                    2G Offline PWA & WhatsApp Bot
                                </div>
                                <p class="text-slate-600 text-[11px]">Rural village chemists log inventory and confirm emergency indents in 30 seconds via WhatsApp voice/text bots.</p>
                            </div>
                        </div>

                        <div class="pt-2 border-t border-slate-100 flex justify-between items-center text-[11px] text-slate-500 font-medium">
                            <span>Sponsor: G.R. Dhanuka Group</span>
                            <span class="text-emerald-600 font-bold">GxP & DPDP Act Ready</span>
                        </div>
                    </div>
                </div>

            </div>
        </section>

        <!-- KPI Strip -->
        <section class="max-w-7xl mx-auto px-6">
            <div class="grid grid-cols-2 md:grid-cols-5 gap-4">
                <div class="card-base p-4 rounded-xl">
                    <div class="flex items-center justify-between text-slate-500 text-xs mb-1">
                        <span>Network In-Stock Rate</span>
                        <i data-lucide="shield-check" class="w-4 h-4 text-emerald-600"></i>
                    </div>
                    <div class="text-2xl font-extrabold text-slate-900" id="kpiInStock">96.4%</div>
                    <div class="text-[11px] text-emerald-600 font-semibold flex items-center mt-1">
                        <i data-lucide="trending-up" class="w-3 h-3 mr-1"></i> +18.2% vs Baseline
                    </div>
                </div>

                <div class="card-base p-4 rounded-xl">
                    <div class="flex items-center justify-between text-slate-500 text-xs mb-1">
                        <span>Forecast Error (MAPE)</span>
                        <i data-lucide="target" class="w-4 h-4 text-blue-600"></i>
                    </div>
                    <div class="text-2xl font-extrabold text-blue-600">11.2%</div>
                    <div class="text-[11px] text-slate-500 font-medium flex items-center mt-1">
                        <span>TFT Deep Model (was 36.5%)</span>
                    </div>
                </div>

                <div class="card-base p-4 rounded-xl">
                    <div class="flex items-center justify-between text-slate-500 text-xs mb-1">
                        <span>Corridor Hazard Alerts</span>
                        <i data-lucide="alert-triangle" class="w-4 h-4 text-amber-600"></i>
                    </div>
                    <div class="text-2xl font-extrabold text-amber-600" id="kpiAlerts">2 Active</div>
                    <div class="text-[11px] text-amber-700 font-medium flex items-center mt-1 truncate">
                        <span>NH-6 (Barak) & NH-29</span>
                    </div>
                </div>

                <div class="card-base p-4 rounded-xl">
                    <div class="flex items-center justify-between text-slate-500 text-xs mb-1">
                        <span>Near-Expiry Rebalanced</span>
                        <i data-lucide="refresh-cw" class="w-4 h-4 text-purple-600"></i>
                    </div>
                    <div class="text-2xl font-extrabold text-purple-700" id="kpiRebalanced">1,420 pk</div>
                    <div class="text-[11px] text-emerald-600 font-semibold flex items-center mt-1">
                        <span>₹3.82L Waste Averted</span>
                    </div>
                </div>

                <div class="card-base p-4 rounded-xl">
                    <div class="flex items-center justify-between text-slate-500 text-xs mb-1">
                        <span>Connected Stockist Hubs</span>
                        <i data-lucide="truck" class="w-4 h-4 text-slate-700"></i>
                    </div>
                    <div class="text-2xl font-extrabold text-slate-900">48 Nodes</div>
                    <div class="text-[11px] text-slate-500 font-medium flex items-center mt-1">
                        <span>Assam + 7 NE States</span>
                    </div>
                </div>
            </div>
        </section>

        <!-- Upper Section: Interactive GIS Map & Corridor Hazard Monitor -->
        <section id="radarSection" class="max-w-7xl mx-auto px-6 space-y-4">
            <div class="flex items-center justify-between">
                <div>
                    <h2 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                        <i data-lucide="map-pin" class="w-5 h-5 text-blue-600"></i>
                        <span>Northeast India Supply Chain & Transit Corridor Radar</span>
                    </h2>
                    <p class="text-xs text-slate-500 font-medium">Real-time status across G.R. Dhanuka Group central depots and peripheral district stockists</p>
                </div>
                <div class="flex items-center space-x-2 text-xs">
                    <span class="inline-flex items-center px-2.5 py-1 rounded-full bg-emerald-50 text-emerald-700 border border-emerald-200 font-semibold">
                        <span class="w-2 h-2 rounded-full bg-emerald-500 mr-1.5"></span> Normal Transit
                    </span>
                    <span class="inline-flex items-center px-2.5 py-1 rounded-full bg-amber-50 text-amber-700 border border-amber-200 font-semibold">
                        <span class="w-2 h-2 rounded-full bg-amber-500 mr-1.5"></span> Caution / Landslide
                    </span>
                    <span class="inline-flex items-center px-2.5 py-1 rounded-full bg-rose-50 text-rose-700 border border-rose-200 font-semibold">
                        <span class="w-2 h-2 rounded-full bg-rose-500 mr-1.5"></span> Flood Washout Risk
                    </span>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Left: GIS Map -->
                <div class="lg:col-span-8 card-base rounded-2xl p-4 flex flex-col space-y-3">
                    <div id="supplyMap"></div>
                    <div class="text-[11px] text-slate-600 flex justify-between items-center bg-slate-50 px-3 py-2 rounded-lg border border-slate-200">
                        <span>Click any marker to inspect depot stock availability, lead-time variance, and critical SKU buffer health.</span>
                        <span class="text-blue-700 font-mono font-semibold">Telemetry: ASDMA & CWC Flood Feeds</span>
                    </div>
                </div>

                <!-- Right: Node Inspection & Emergency Indent Trigger -->
                <div class="lg:col-span-4 card-base rounded-2xl p-5 flex flex-col space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                        <h3 class="text-sm font-bold text-slate-900 flex items-center gap-1.5">
                            <i data-lucide="package" class="w-4 h-4 text-blue-600"></i>
                            <span id="selectedNodeTitle">Silchar Buffer Depot (Barak Valley)</span>
                        </h3>
                        <span id="selectedNodeBadge" class="text-[10px] px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold">Vulnerable Corridor</span>
                    </div>

                    <div class="space-y-3 flex-1 overflow-y-auto">
                        <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 text-xs space-y-1.5">
                            <div class="flex justify-between text-slate-600">
                                <span>Corridor Transit Link:</span>
                                <span class="text-slate-900 font-semibold">NH-6 via Meghalaya</span>
                            </div>
                            <div class="flex justify-between text-slate-600">
                                <span>Predicted Lead Time:</span>
                                <span class="text-amber-700 font-bold" id="nodeLeadTime">18 - 25 Days (Flood Spike)</span>
                            </div>
                            <div class="flex justify-between text-slate-600">
                                <span>Current Stock Runway:</span>
                                <span class="text-rose-600 font-bold" id="nodeRunway">11.4 Days (Deficit Risk)</span>
                            </div>
                            <div class="flex justify-between text-slate-600">
                                <span>Target Pre-Monsoon Buffer:</span>
                                <span class="text-blue-700 font-bold" id="nodeTargetBuffer">35 Days</span>
                            </div>
                        </div>

                        <h4 class="text-xs font-bold text-slate-800 uppercase tracking-wider">Critical SKU Stock Health</h4>
                        
                        <div class="space-y-2 text-xs" id="skuStatusList">
                            <div class="p-3 rounded-xl bg-white border border-slate-200 shadow-sm flex items-center justify-between">
                                <div>
                                    <div class="font-bold text-slate-900">Polyvalent Anti-Snake Venom (10ml)</div>
                                    <div class="text-[11px] text-slate-500">Vital Emergency · Batch #ASV-882</div>
                                </div>
                                <div class="text-right">
                                    <span class="px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold text-[10px]">Critical (8 vials)</span>
                                    <div class="text-[10px] text-slate-500 font-medium mt-0.5">Need: +250 vials</div>
                                </div>
                            </div>

                            <div class="p-3 rounded-xl bg-white border border-slate-200 shadow-sm flex items-center justify-between">
                                <div>
                                    <div class="font-bold text-slate-900">Human Regular Insulin 40IU/ml</div>
                                    <div class="text-[11px] text-slate-500">Chronic · 2°C–8°C Cold Chain</div>
                                </div>
                                <div class="text-right">
                                    <span class="px-2 py-0.5 rounded bg-amber-50 text-amber-700 border border-amber-200 font-bold text-[10px]">Low (42 vials)</span>
                                    <div class="text-[10px] text-slate-500 font-medium mt-0.5">Need: +120 vials</div>
                                </div>
                            </div>

                            <div class="p-3 rounded-xl bg-white border border-slate-200 shadow-sm flex items-center justify-between">
                                <div>
                                    <div class="font-bold text-slate-900">Cefixime Oral Susp 100mg/5ml</div>
                                    <div class="text-[11px] text-slate-500">Pediatric Antibiotic Formulation</div>
                                </div>
                                <div class="text-right">
                                    <span class="px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold text-[10px]">Healthy (480 pk)</span>
                                    <div class="text-[10px] text-slate-500 font-medium mt-0.5">Runway: 28 Days</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="pt-2 border-t border-slate-100">
                        <button id="dispatchIndentBtn" onclick="dispatchEmergencyIndent()" class="w-full py-2.5 px-3 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs shadow-md shadow-blue-600/20 flex items-center justify-center space-x-1.5 transition">
                            <i data-lucide="send" class="w-3.5 h-3.5"></i>
                            <span>Auto-Generate Pre-Positioning Dispatch</span>
                        </button>
                        <div id="dispatchSuccessMsg" class="hidden text-center text-xs text-emerald-600 mt-2 font-bold bg-emerald-50 p-2 rounded-lg border border-emerald-200">
                            ✓ Transfer PO #DHN-2026-9041 pushed to Dhanuka Central ERP!
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- Middle Section: AI Forecasting Studio & Scenario Simulator -->
        <section id="forecastSection" class="max-w-7xl mx-auto px-6 space-y-4">
            <div class="flex items-center justify-between">
                <div>
                    <h2 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                        <i data-lucide="line-chart" class="w-5 h-5 text-blue-600"></i>
                        <span>Temporal Fusion Transformer (TFT) 90-Day Probabilistic Demand Forecast</span>
                    </h2>
                    <p class="text-xs text-slate-500 font-medium">SKU: Amoxicillin + Pot. Clavulanate 625mg & IV Fluids (Combined Monsoon Surge Cohort)</p>
                </div>
                <div class="flex items-center space-x-2 text-xs">
                    <button class="px-3 py-1 rounded-lg bg-white border border-slate-200 text-slate-700 font-semibold shadow-sm">Upper Assam</button>
                    <button class="px-3 py-1 rounded-lg bg-blue-50 border border-blue-200 text-blue-700 font-bold">Barak Valley & Hill Nodes</button>
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Forecast Chart -->
                <div class="lg:col-span-8 card-base rounded-2xl p-5 flex flex-col justify-between">
                    <div class="flex-1 min-h-[300px]">
                        <canvas id="forecastChart"></canvas>
                    </div>

                    <div class="mt-4 pt-3 border-t border-slate-100 flex flex-wrap items-center justify-between text-xs text-slate-600 gap-2">
                        <div class="flex items-center space-x-4">
                            <span class="flex items-center font-medium"><span class="w-3 h-1 bg-slate-400 mr-1.5 rounded"></span> Historical Sales</span>
                            <span class="flex items-center font-medium"><span class="w-3 h-1 bg-blue-600 mr-1.5 rounded"></span> P50 Median Forecast</span>
                            <span class="flex items-center font-medium"><span class="w-3 h-2 bg-blue-100 mr-1.5 rounded"></span> P10-P90 Confidence Band</span>
                        </div>
                        <span class="text-blue-700 font-mono font-bold">Quantile Loss: 0.042 (TFT Best)</span>
                    </div>
                </div>

                <!-- Simulation Controls -->
                <div class="lg:col-span-4 card-base rounded-2xl p-5 flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center space-x-2 border-b border-slate-100 pb-2 mb-4">
                            <i data-lucide="sliders" class="w-4 h-4 text-emerald-600"></i>
                            <h3 class="text-sm font-bold text-slate-900">Scenario Simulation Engine</h3>
                        </div>

                        <div class="space-y-4 text-xs">
                            <div>
                                <div class="flex justify-between mb-1.5">
                                    <span class="text-slate-700 font-semibold">Monsoon / Flood Severity Index</span>
                                    <span class="text-blue-700 font-bold" id="floodVal">Level 4 (Severe Washouts)</span>
                                </div>
                                <input type="range" min="1" max="5" value="4" class="w-full accent-blue-600 cursor-pointer" id="floodSlider" oninput="updateScenario()">
                                <div class="flex justify-between text-[10px] text-slate-400 mt-0.5">
                                    <span>Normal</span>
                                    <span>Moderate</span>
                                    <span>Peak Inundation</span>
                                </div>
                            </div>

                            <div>
                                <div class="flex justify-between mb-1.5">
                                    <span class="text-slate-700 font-semibold">Epidemic Outbreak Factor (IDSP)</span>
                                    <span class="text-amber-700 font-bold" id="outbreakVal">+45% (JE & Dengue Surge)</span>
                                </div>
                                <input type="range" min="0" max="100" value="45" class="w-full accent-amber-600 cursor-pointer" id="outbreakSlider" oninput="updateScenario()">
                                <div class="flex justify-between text-[10px] text-slate-400 mt-0.5">
                                    <span>Baseline</span>
                                    <span>+50% Surge</span>
                                    <span>+100% Dual Epidemic</span>
                                </div>
                            </div>

                            <div>
                                <div class="flex justify-between mb-1.5">
                                    <span class="text-slate-700 font-semibold">Transit Corridor Delay Add-on</span>
                                    <span class="text-rose-700 font-bold" id="delayVal">+16 Days</span>
                                </div>
                                <input type="range" min="0" max="30" value="16" class="w-full accent-rose-600 cursor-pointer" id="delaySlider" oninput="updateScenario()">
                                <div class="flex justify-between text-[10px] text-slate-400 mt-0.5">
                                    <span>0 Days</span>
                                    <span>+15 Days</span>
                                    <span>+30 Days Bridge Washout</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="bg-blue-50/70 p-4 rounded-xl border border-blue-200 text-xs space-y-2">
                        <div class="text-blue-900 font-bold flex items-center gap-1.5">
                            <i data-lucide="cpu" class="w-4 h-4 text-blue-600"></i>
                            <span>MEIO Buffer Recommendation:</span>
                        </div>
                        <div class="text-slate-700 text-[11px] leading-relaxed">
                            Under simulated parameters, replenish <strong class="text-blue-800">+4,200 packs</strong> before Day 14 to avert a projected <strong class="text-rose-700 font-bold">42% stockout crisis</strong> in Barak Valley.
                        </div>
                        <button onclick="applyOptimizedPlan()" class="w-full py-2 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold text-xs transition shadow-sm">
                            Apply MILP Optimal Allocation
                        </button>
                    </div>
                </div>
            </div>
        </section>

        <!-- Lower Section: Expiry Arbitrage Matrix & Rural WhatsApp Bot Simulator -->
        <section class="max-w-7xl mx-auto px-6 space-y-4 pb-12">
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                
                <!-- FEFO Expiry Arbitrage Table -->
                <div class="lg:col-span-7 card-base rounded-2xl p-5 flex flex-col space-y-3">
                    <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
                        <div class="flex items-center space-x-2">
                            <i data-lucide="arrow-left-right" class="w-4 h-4 text-purple-600"></i>
                            <h3 class="text-sm font-bold text-slate-900">Cross-Tier Expiry Arbitrage & Rebalancing Matrix</h3>
                        </div>
                        <span class="text-xs text-purple-700 bg-purple-50 px-2 py-0.5 rounded border border-purple-200 font-bold">FEFO Active</span>
                    </div>

                    <p class="text-xs text-slate-500">The algorithm automatically identifies slow-moving batches nearing 6-month expiry at low-velocity stockists and re-routes them to high-consumption hospital wards.</p>

                    <div class="overflow-x-auto">
                        <table class="w-full text-left text-xs">
                            <thead>
                                <tr class="text-slate-500 border-b border-slate-200 text-[11px]">
                                    <th class="pb-2 font-bold">Batch / SKU</th>
                                    <th class="pb-2 font-bold">Origin Depot</th>
                                    <th class="pb-2 font-bold">Expiry</th>
                                    <th class="pb-2 font-bold">Qty</th>
                                    <th class="pb-2 font-bold">Recommended Destination</th>
                                    <th class="pb-2 font-bold text-right">Action</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-slate-100" id="arbitrageTable">
                                <tr class="hover:bg-slate-50">
                                    <td class="py-2.5 font-bold text-slate-900">
                                        #ARB-204 · Rabies Antiserum 1000IU
                                    </td>
                                    <td class="py-2.5 text-slate-600">Tezpur Sub-Depot (Slow)</td>
                                    <td class="py-2.5 text-amber-700 font-bold font-mono">4.5 Mos</td>
                                    <td class="py-2.5 text-slate-800 font-medium">180 vials</td>
                                    <td class="py-2.5 text-emerald-700 font-bold">Silchar Civil Hospital (High)</td>
                                    <td class="py-2.5 text-right">
                                        <button onclick="executeRebalance(this, 'ARB-204')" class="px-2.5 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-[11px] font-semibold transition">
                                            Rebalance
                                        </button>
                                    </td>
                                </tr>

                                <tr class="hover:bg-slate-50">
                                    <td class="py-2.5 font-bold text-slate-900">
                                        #CTX-911 · Ceftriaxone 1g Inj
                                    </td>
                                    <td class="py-2.5 text-slate-600">Jorhat Wholesaler</td>
                                    <td class="py-2.5 text-amber-700 font-bold font-mono">5.2 Mos</td>
                                    <td class="py-2.5 text-slate-800 font-medium">640 vials</td>
                                    <td class="py-2.5 text-emerald-700 font-bold">Guwahati Medical College Node</td>
                                    <td class="py-2.5 text-right">
                                        <button onclick="executeRebalance(this, 'CTX-911')" class="px-2.5 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-[11px] font-semibold transition">
                                            Rebalance
                                        </button>
                                    </td>
                                </tr>

                                <tr class="hover:bg-slate-50">
                                    <td class="py-2.5 font-bold text-slate-900">
                                        #ORS-502 · Oral Rehydration Salts
                                    </td>
                                    <td class="py-2.5 text-slate-600">Shillong Retail Cohort</td>
                                    <td class="py-2.5 text-amber-700 font-bold font-mono">6.0 Mos</td>
                                    <td class="py-2.5 text-slate-800 font-medium">1,200 sachet</td>
                                    <td class="py-2.5 text-emerald-700 font-bold">Dhubri Flood Relief Clinic</td>
                                    <td class="py-2.5 text-right">
                                        <button onclick="executeRebalance(this, 'ORS-502')" class="px-2.5 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded-lg text-[11px] font-semibold transition">
                                            Rebalance
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Rural Chemist WhatsApp Bot Mockup -->
                <div class="lg:col-span-5 card-base rounded-2xl p-5 flex flex-col space-y-3">
                    <div class="flex items-center justify-between border-b border-slate-100 pb-2.5">
                        <div class="flex items-center space-x-2">
                            <i data-lucide="message-square" class="w-4 h-4 text-emerald-600"></i>
                            <h3 class="text-sm font-bold text-slate-900">Rural Chemist WhatsApp Conversational Bot</h3>
                        </div>
                        <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold">2G / Offline Capable</span>
                    </div>

                    <!-- Chat Display -->
                    <div class="bg-slate-100 rounded-xl p-3 flex-1 min-h-[220px] max-h-[240px] overflow-y-auto space-y-2.5 text-xs font-sans border border-slate-200" id="chatWindow">
                        <div class="flex items-start space-x-2">
                            <div class="w-6 h-6 rounded-full bg-emerald-600 flex items-center justify-center text-[10px] font-bold text-white">MB</div>
                            <div class="bg-white text-slate-800 p-2.5 rounded-xl rounded-tl-none max-w-[85%] border border-slate-200 shadow-sm">
                                Namaskar Borthakur Medicos (Silchar)! MediFlow Bot here. Our flood forecast indicates NH-6 delivery delays starting next week. Please confirm current Paracetamol and Anti-venom stocks.
                                <div class="text-[9px] text-slate-400 mt-1">10:42 AM · Dhanuka Logistics Bot</div>
                            </div>
                        </div>

                        <div class="flex items-start justify-end space-x-2">
                            <div class="bg-emerald-600 text-white p-2.5 rounded-xl rounded-tr-none max-w-[85%] shadow-sm">
                                Paracetamol syrup 60ml: only 12 bottles left. Need 150 bottles before roads close.
                                <div class="text-[9px] text-emerald-100 mt-1 text-right">10:44 AM · Chemist</div>
                            </div>
                        </div>

                        <div class="flex items-start space-x-2">
                            <div class="w-6 h-6 rounded-full bg-emerald-600 flex items-center justify-center text-[10px] font-bold text-white">MB</div>
                            <div class="bg-white text-slate-800 p-2.5 rounded-xl rounded-tl-none max-w-[85%] border border-slate-200 shadow-sm">
                                ✓ Requisition #ORD-7721 confirmed! 150 bottles routed from Silchar Buffer Depot. Delivery scheduled for tomorrow morning via priority transit.
                                <div class="text-[9px] text-slate-400 mt-1">10:44 AM · Auto PO Logged</div>
                            </div>
                        </div>
                    </div>

                    <!-- Chat Input Mockup -->
                    <div class="flex items-center space-x-2">
                        <input type="text" id="chatInput" placeholder="Type message (e.g. 'Stock Cefixime: 5 packs left')..." class="flex-1 bg-white border border-slate-300 rounded-xl px-3 py-2 text-xs text-slate-900 placeholder-slate-400 focus:outline-none focus:border-blue-500 shadow-sm">
                        <button onclick="sendChatMessage()" class="px-3.5 py-2 bg-emerald-600 hover:bg-emerald-700 text-white rounded-xl text-xs font-bold flex items-center space-x-1 shadow-sm transition">
                            <span>Send</span>
                            <i data-lucide="send" class="w-3 h-3"></i>
                        </button>
                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-white border-t border-slate-200 px-6 py-6 text-xs text-slate-500 flex flex-wrap justify-between items-center gap-4 shadow-sm">
        <div>
            Developed for <strong class="text-slate-900">North East Seva First Innovation Challenge (NESFIC 2026)</strong> | Problem Statement <strong>NESFIC-I-09</strong>
        </div>
        <div class="flex items-center space-x-4">
            <span>Sponsoring Partner: <strong class="text-blue-700 font-bold">G.R. Dhanuka Group</strong></span>
            <span>Grant Allocation: <strong class="text-emerald-700 font-bold">₹40.00 Lakhs Total</strong> (₹20.00 Lakhs Tech Team)</span>
        </div>
    </footer>

    <!-- Tutorial / Walkthrough Modal (White Aesthetic) -->
    <div id="tutorialModal" class="hidden fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
        <div class="bg-white border border-slate-200 rounded-2xl max-w-3xl w-full p-6 shadow-2xl space-y-5 text-slate-800 my-8">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                <div class="flex items-center space-x-3">
                    <div class="w-9 h-9 rounded-xl bg-amber-50 border border-amber-200 flex items-center justify-center text-amber-600">
                        <i data-lucide="book-open" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <h3 class="text-base font-bold text-slate-900">MediFlow-NE: Interactive System Tutorial & User Guide</h3>
                        <p class="text-xs text-slate-500">Understanding the AI Supply Chain Platform for G.R. Dhanuka Group (NESFIC-I-09)</p>
                    </div>
                </div>
                <button onclick="closeTutorialModal()" class="text-slate-400 hover:text-slate-700 p-1 rounded-lg">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>

            <!-- Tutorial Content -->
            <div class="space-y-4 text-xs max-h-[65vh] overflow-y-auto pr-2">
                <div class="bg-blue-50 border border-blue-200 p-3.5 rounded-xl text-blue-900 leading-relaxed">
                    <strong class="text-blue-950 flex items-center gap-1.5 mb-1">
                        <i data-lucide="info" class="w-4 h-4 text-blue-600"></i>
                        The Regional Problem (NESFIC-I-09):
                    </strong>
                    Northeast India faces severe logistics bottlenecks due to seasonal Brahmaputra floods and landslides cutting key highway corridors (NH-6 to Barak Valley, NH-29 to Nagaland). Central warehouses in Guwahati lack visibility into peripheral chemists, causing <strong>25–34% stockouts of life-saving medicines</strong> during monsoons, while urban stockists face <strong>6–9% near-expiry wastage</strong>.
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="font-bold text-blue-800 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-[10px]">1</span>
                            Interactive GIS Logistics Radar
                        </div>
                        <p class="text-slate-600">Explore the interactive map of Northeast India. Click any hub (Guwahati, Silchar, Dibrugarh, Tezpur) to inspect lead-time variations, live flood hazard warnings along NH-6, and stock runway for vital medicines.</p>
                    </div>

                    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="font-bold text-blue-800 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-[10px]">2</span>
                            AI Forecast & Scenario Studio
                        </div>
                        <p class="text-slate-600">Powered by Temporal Fusion Transformers (TFT). Adjust the <strong>Monsoon Severity</strong>, <strong>Epidemic Outbreak</strong>, and <strong>Transit Delay</strong> sliders to watch the demand forecast curve dynamically adapt in real-time.</p>
                    </div>

                    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="font-bold text-blue-800 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-[10px]">3</span>
                            FEFO Expiry Arbitrage Matrix
                        </div>
                        <p class="text-slate-600">The platform automatically detects slow-moving batches nearing 6 months of expiry. Click <strong>"Rebalance"</strong> in the table to dynamically simulate transferring them to high-velocity emergency wards.</p>
                    </div>

                    <div class="p-3.5 rounded-xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="font-bold text-blue-800 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-blue-100 text-blue-700 flex items-center justify-center text-[10px]">4</span>
                            Rural Chemist WhatsApp Bot
                        </div>
                        <p class="text-slate-600">Type a test message (e.g. <em>"Stock Cefixime: 5 packs left"</em>) in the mobile chat panel to experience how rural pharmacies with spotty 2G internet can log stock and confirm emergency replenishments in under 30 seconds.</p>
                    </div>
                </div>

                <div class="p-3.5 rounded-xl bg-purple-50 border border-purple-200 space-y-1.5">
                    <div class="font-bold text-purple-900 flex items-center gap-1.5">
                        <span class="w-5 h-5 rounded-full bg-purple-100 text-purple-700 flex items-center justify-center text-[10px]">5</span>
                        Admin Command & Control Center
                    </div>
                    <p class="text-slate-700">Click <strong>"Admin Console (Login)"</strong> in the top header. Use demo credentials (<code>admin@dhanuka.com</code> / <code>dhanuka2026</code>) to unlock route hazard management, buffer rule tuning, stockist ERP sync health, and GxP audit logs.</p>
                </div>
            </div>

            <div class="pt-3 border-t border-slate-100 flex justify-between items-center text-xs">
                <span class="text-slate-500 font-medium">NESFIC 2026 | Sponsoring Partner: G.R. Dhanuka Group</span>
                <button onclick="closeTutorialModal()" class="px-4 py-2 rounded-xl bg-blue-600 hover:bg-blue-700 text-white font-bold transition">
                    Got it, Let's Explore!
                </button>
            </div>
        </div>
    </div>

    <!-- Admin Login Modal (White Aesthetic) -->
    <div id="adminLoginModal" class="hidden fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="bg-white border border-slate-200 rounded-2xl max-w-md w-full p-6 shadow-2xl space-y-4 text-slate-800">
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                <div class="flex items-center space-x-2.5">
                    <div class="w-8 h-8 rounded-xl bg-purple-50 border border-purple-200 flex items-center justify-center text-purple-600">
                        <i data-lucide="shield" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-slate-900">Dhanuka Logistics Admin Login</h3>
                        <p class="text-[11px] text-slate-500">Secure Access to MediFlow-NE Command Console</p>
                    </div>
                </div>
                <button onclick="closeAdminLoginModal()" class="text-slate-400 hover:text-slate-700 p-1 rounded-lg">
                    <i data-lucide="x" class="w-4 h-4"></i>
                </button>
            </div>

            <!-- Demo Credentials Banner -->
            <div class="bg-purple-50 border border-purple-200 p-3 rounded-xl text-xs space-y-1">
                <div class="flex justify-between items-center">
                    <span class="text-purple-900 font-bold">Demo Admin Credentials:</span>
                    <button onclick="fillDemoCredentials()" class="text-[10px] bg-purple-600 hover:bg-purple-700 text-white px-2 py-0.5 rounded font-medium transition">
                        ⚡ Quick Fill
                    </button>
                </div>
                <div class="text-[11px] text-slate-700 font-mono">
                    User: <strong class="text-purple-950 font-bold">admin@dhanuka.com</strong><br/>
                    Pass: <strong class="text-purple-950 font-bold">dhanuka2026</strong>
                </div>
            </div>

            <form onsubmit="handleAdminLogin(event)" class="space-y-3 text-xs">
                <div>
                    <label class="block text-slate-700 mb-1 font-semibold">Username / Work Email</label>
                    <input type="text" id="adminEmailInput" required placeholder="admin@dhanuka.com" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-slate-900 focus:outline-none focus:border-purple-500 shadow-sm">
                </div>
                <div>
                    <label class="block text-slate-700 mb-1 font-semibold">Password</label>
                    <input type="password" id="adminPassInput" required placeholder="••••••••••••" class="w-full bg-white border border-slate-300 rounded-xl px-3 py-2 text-slate-900 focus:outline-none focus:border-purple-500 shadow-sm">
                </div>
                <div id="loginErrorMsg" class="hidden text-rose-600 text-[11px] font-bold">
                    Invalid credentials. Please use the demo credentials above.
                </div>
                <button type="submit" class="w-full py-2.5 rounded-xl bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs shadow-md shadow-purple-600/20 transition">
                    Sign In to Admin Console
                </button>
            </form>
        </div>
    </div>

    <!-- Admin Panel Full Modal (White Aesthetic) -->
    <div id="adminPanelModal" class="hidden fixed inset-0 z-50 bg-black/60 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
        <div class="bg-white border border-slate-200 rounded-2xl max-w-5xl w-full p-6 shadow-2xl space-y-5 text-slate-800 my-6">
            
            <!-- Modal Header -->
            <div class="flex items-center justify-between border-b border-slate-100 pb-3">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-purple-50 border border-purple-200 flex items-center justify-center text-purple-600">
                        <i data-lucide="shield-check" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h3 class="text-base font-bold text-slate-900">Dhanuka Central Admin Command Console</h3>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold font-mono">Role: SCM Enterprise Admin</span>
                        </div>
                        <p class="text-xs text-slate-500 font-medium">Network Hazards, SKU Buffer Rules, ERP Gateways, Indent Approvals & GxP Audit Ledger</p>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <button onclick="handleAdminLogout()" class="px-2.5 py-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-rose-600 text-xs font-semibold border border-slate-200 flex items-center gap-1.5 transition">
                        <i data-lucide="log-out" class="w-3.5 h-3.5"></i>
                        <span>Logout</span>
                    </button>
                    <button onclick="closeAdminPanelModal()" class="text-slate-400 hover:text-slate-700 p-1 rounded-lg">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>
            </div>

            <!-- Tab Navigation Bar -->
            <div class="flex items-center space-x-1 border-b border-slate-200 text-xs overflow-x-auto pb-1">
                <button onclick="switchAdminTab('corridors')" id="tabBtn-corridors" class="px-3.5 py-2 font-bold rounded-lg bg-purple-50 text-purple-800 border border-purple-200 flex items-center gap-1.5 transition">
                    <i data-lucide="truck" class="w-4 h-4"></i>
                    <span>Corridor Hazards & Routes</span>
                </button>
                <button onclick="switchAdminTab('skus')" id="tabBtn-skus" class="px-3.5 py-2 font-medium rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1.5 transition">
                    <i data-lucide="package" class="w-4 h-4"></i>
                    <span>Master SKU & Buffer Policies</span>
                </button>
                <button onclick="switchAdminTab('stockists')" id="tabBtn-stockists" class="px-3.5 py-2 font-medium rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1.5 transition">
                    <i data-lucide="database" class="w-4 h-4"></i>
                    <span>Stockist ERP Network</span>
                </button>
                <button onclick="switchAdminTab('dispatches')" id="tabBtn-dispatches" class="px-3.5 py-2 font-medium rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1.5 transition">
                    <i data-lucide="check-circle" class="w-4 h-4"></i>
                    <span>AI Dispatch Approvals <span id="pendingIndentCountBadge" class="ml-1 px-1.5 py-0.2 rounded-full bg-blue-100 text-blue-700 font-bold text-[10px]">3</span></span>
                </button>
                <button onclick="switchAdminTab('audit')" id="tabBtn-audit" class="px-3.5 py-2 font-medium rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1.5 transition">
                    <i data-lucide="file-check" class="w-4 h-4"></i>
                    <span>GxP Audit & Batch Recall</span>
                </button>
            </div>

            <!-- Tab 1: Corridors & Hazards -->
            <div id="adminTab-corridors" class="space-y-4 text-xs max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-center justify-between">
                    <div>
                        <h4 class="text-sm font-bold text-slate-900">Regional Transit Corridor Vulnerability Manager</h4>
                        <p class="text-slate-500">Override real-time environmental disruption telemetry to trigger automated network-wide replenishment recalculations.</p>
                    </div>
                    <button onclick="resetCorridorDefaults()" class="px-2.5 py-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-700 text-[11px] font-semibold border border-slate-200">
                        Reset Telemetry
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                    <!-- Corridor 1: NH-6 -->
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-slate-900 text-sm">NH-6: Guwahati ➔ Shillong ➔ Silchar</div>
                                <div class="text-slate-500 text-[11px]">Barak Valley, Tripura & Mizoram Lifeline Corridor</div>
                            </div>
                            <span id="adminNH6Badge" class="text-[10px] px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold">Flood Hazard Active</span>
                        </div>
                        <div class="flex justify-between text-slate-700 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-rose-600 font-bold" id="adminNH6Days">18 - 25 Days (+16d Delay)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="toggleRouteStatus('nh6')" class="w-full py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs transition">
                                Toggle Road Status (Clear / Flood)
                            </button>
                        </div>
                    </div>

                    <!-- Corridor 2: NH-29 -->
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-slate-900 text-sm">NH-29: Tezpur ➔ Dimapur ➔ Kohima</div>
                                <div class="text-slate-500 text-[11px]">Nagaland & Manipur Mountain Transit Highway</div>
                            </div>
                            <span id="adminNH29Badge" class="text-[10px] px-2 py-0.5 rounded bg-amber-50 text-amber-700 border border-amber-200 font-bold">Landslide Caution</span>
                        </div>
                        <div class="flex justify-between text-slate-700 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-amber-700 font-bold" id="adminNH29Days">7 - 10 Days (+4d Delay)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="toggleRouteStatus('nh29')" class="w-full py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold text-xs transition">
                                Toggle Road Status (Clear / Caution)
                            </button>
                        </div>
                    </div>

                    <!-- Corridor 3: NH-27 -->
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-slate-900 text-sm">NH-27: Guwahati ➔ Tezpur ➔ Dibrugarh</div>
                                <div class="text-slate-500 text-[11px]">East-West Four-Lane Arterial (Upper Assam)</div>
                            </div>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold">Clear & Optimal</span>
                        </div>
                        <div class="flex justify-between text-slate-700 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-emerald-700 font-bold">3 - 5 Days (Nominal)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="alert('NH-27 status confirmed: In-transit telemetry clear.')" class="w-full py-1.5 rounded-lg bg-slate-200 hover:bg-slate-300 text-slate-800 font-semibold text-xs transition">
                                Run Diagnostics
                            </button>
                        </div>
                    </div>

                    <!-- Corridor 4: Brahmaputra Riverine / Island Routes -->
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-slate-900 text-sm">Brahmaputra Riverine Crossing (Majuli Hub)</div>
                                <div class="text-slate-500 text-[11px]">Ferry-Dependent Island Clinics & Riverine PHCs</div>
                            </div>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-amber-50 text-amber-700 border border-amber-200 font-bold">Ferry Suspended</span>
                        </div>
                        <div class="flex justify-between text-slate-700 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-amber-700 font-bold">High Water Delays (+10d)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="alert('Drone emergency corridor activated for Majuli riverine dispatch!')" class="w-full py-1.5 rounded-lg bg-purple-600 hover:bg-purple-700 text-white font-bold text-xs transition">
                                Activate Emergency Drone Corridor
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 2: Master SKU & Buffer Policies -->
            <div id="adminTab-skus" class="hidden space-y-4 text-xs max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-center justify-between">
                    <div>
                        <h4 class="text-sm font-bold text-slate-900">Pharmaceutical Master SKU Catalog & Dynamic Buffer Rules</h4>
                        <p class="text-slate-500">Configure ABC-VED priorities, storage conditions, and seasonal pre-monsoon safety buffers.</p>
                    </div>
                    <button onclick="alert('New SKU wizard initialized! Ingesting barcode schema...')" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-700 text-white font-bold flex items-center gap-1.5">
                        <i data-lucide="plus-circle" class="w-3.5 h-3.5"></i>
                        <span>Add New SKU</span>
                    </button>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left">
                        <thead>
                            <tr class="text-slate-500 border-b border-slate-200 text-[11px]">
                                <th class="pb-2 font-bold">SKU Code / Description</th>
                                <th class="pb-2 font-bold">ABC-VED Tag</th>
                                <th class="pb-2 font-bold">Storage Spec</th>
                                <th class="pb-2 font-bold">Standard Buffer</th>
                                <th class="pb-2 font-bold">Monsoon Pre-Position Buffer</th>
                                <th class="pb-2 font-bold text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100" id="skuMasterTable">
                            <tr class="hover:bg-slate-50">
                                <td class="py-2.5 font-bold text-slate-900">
                                    #SKU-001 · Polyvalent Anti-Snake Venom (10ml)
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold text-[10px]">Vital (V)</span></td>
                                <td class="py-2.5 text-blue-700 font-mono font-bold">2°C–8°C Cold Chain</td>
                                <td class="py-2.5 text-slate-700">21 Days</td>
                                <td class="py-2.5 text-emerald-700 font-bold">35 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated: 35 days enforced for Assam floods.')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-800 rounded font-semibold text-[10px]">Edit Rule</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="py-2.5 font-bold text-slate-900">
                                    #SKU-002 · Human Regular Insulin 40IU/ml
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold text-[10px]">Vital (V)</span></td>
                                <td class="py-2.5 text-blue-700 font-mono font-bold">2°C–8°C Cold Chain</td>
                                <td class="py-2.5 text-slate-700">21 Days</td>
                                <td class="py-2.5 text-emerald-700 font-bold">28 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated.')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-800 rounded font-semibold text-[10px]">Edit Rule</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-50">
                                <td class="py-2.5 font-bold text-slate-900">
                                    #SKU-003 · Cefixime Oral Susp 100mg/5ml
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-blue-50 text-blue-700 border border-blue-200 font-bold text-[10px]">Essential (E)</span></td>
                                <td class="py-2.5 text-slate-600">Room Temp (&lt; 25°C)</td>
                                <td class="py-2.5 text-slate-700">14 Days</td>
                                <td class="py-2.5 text-emerald-700 font-bold">28 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated.')" class="px-2.5 py-1 bg-slate-100 hover:bg-slate-200 text-slate-800 rounded font-semibold text-[10px]">Edit Rule</button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Tab 3: Stockist ERP Network & Sync -->
            <div id="adminTab-stockists" class="hidden space-y-4 text-xs max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-center justify-between">
                    <div>
                        <h4 class="text-sm font-bold text-slate-900">Connected Stockist ERP & Ingestion Network (48 Active Nodes)</h4>
                        <p class="text-slate-500">Live heartbeat monitoring of automated data pipelines across Marg ERP, Tally Prime, and Busy installations.</p>
                    </div>
                    <button onclick="triggerForceSyncAll()" class="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-700 text-white font-bold flex items-center gap-1.5 shadow-sm">
                        <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                        <span>Force Sync All Nodes</span>
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                    <div class="bg-slate-50 p-3.5 rounded-xl border border-slate-200 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-slate-900">Guwahati Central C&F</span>
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                        </div>
                        <div class="text-[11px] text-slate-500">Dhanuka Enterprise Core (SAP)</div>
                        <div class="text-[10px] text-emerald-700 font-mono font-bold">Sync: 100% · Latency 140ms</div>
                    </div>

                    <div class="bg-slate-50 p-3.5 rounded-xl border border-slate-200 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-slate-900">Dibrugarh Super Stockist</span>
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                        </div>
                        <div class="text-[11px] text-slate-500">Upper Assam Agency (Marg ERP)</div>
                        <div class="text-[10px] text-emerald-700 font-mono font-bold">Sync: 12 min ago · 410 SKUs</div>
                    </div>

                    <div class="bg-slate-50 p-3.5 rounded-xl border border-slate-200 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-slate-900">Silchar Buffer Depot</span>
                            <span class="w-2.5 h-2.5 rounded-full bg-emerald-500"></span>
                        </div>
                        <div class="text-[11px] text-slate-500">Barak Medicos (Tally Prime)</div>
                        <div class="text-[10px] text-emerald-700 font-mono font-bold">Sync: 24 min ago · 380 SKUs</div>
                    </div>
                </div>

                <div class="bg-slate-50 p-3 rounded-xl border border-slate-200 text-slate-600 text-[11px] flex justify-between items-center font-medium">
                    <span>Zero-Footprint Sync Agent: Compatible with Marg ERP 9.0+, Tally Prime Release 2.0+, and Busy 18/21.</span>
                    <span class="text-blue-700 font-mono font-bold">Total Monitored Ledger Rows: 1,480,240</span>
                </div>
            </div>

            <!-- Tab 4: AI Dispatch Approvals -->
            <div id="adminTab-dispatches" class="hidden space-y-4 text-xs max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-center justify-between">
                    <div>
                        <h4 class="text-sm font-bold text-slate-900">Human-in-the-Loop AI Dispatch & Pre-Positioning Authorization Queue</h4>
                        <p class="text-slate-500">Review, modify, and authorize algorithmic indents before PO creation in Dhanuka SAP core.</p>
                    </div>
                    <span class="text-xs text-amber-800 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200 font-bold font-mono">3 Indents Awaiting Approval</span>
                </div>

                <div class="space-y-3" id="indentCardsContainer">
                    <!-- Indent 1 -->
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 flex flex-wrap items-center justify-between gap-4" id="indentCard-1">
                        <div class="space-y-1 max-w-md">
                            <div class="flex items-center space-x-2">
                                <span class="text-xs font-bold text-slate-900">Indent #REC-401</span>
                                <span class="px-2 py-0.2 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold text-[10px]">High Urgency (Pre-Flood)</span>
                            </div>
                            <div class="text-slate-800 font-bold">Polyvalent Anti-Snake Venom (10ml) ➔ 2,500 Vials</div>
                            <div class="text-slate-600 text-[11px]">Routing: Guwahati Central C&F ➔ Silchar Buffer Depot (Barak Valley)</div>
                            <div class="text-blue-700 text-[10px] font-semibold">AI Model: TFT Quantile P90 Surge · Confidence: 94.6% · Hazard: NH-6 Washout Risk</div>
                        </div>
                        <div class="flex items-center space-x-2">
                            <button onclick="approveIndent('indentCard-1', 'PO-DHN-9901', 'Silchar Buffer Depot')" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs transition shadow-sm">
                                Approve & Issue PO
                            </button>
                            <button onclick="rejectIndent('indentCard-1')" class="px-3 py-2 bg-white hover:bg-slate-100 text-rose-700 border border-slate-200 rounded-xl text-xs font-semibold transition">
                                Reject
                            </button>
                        </div>
                    </div>

                    <!-- Indent 2 -->
                    <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 flex flex-wrap items-center justify-between gap-4" id="indentCard-2">
                        <div class="space-y-1 max-w-md">
                            <div class="flex items-center space-x-2">
                                <span class="text-xs font-bold text-slate-900">Indent #REC-402</span>
                                <span class="px-2 py-0.2 rounded bg-amber-50 text-amber-700 border border-amber-200 font-bold text-[10px]">Seasonal Spurt</span>
                            </div>
                            <div class="text-slate-800 font-bold">Cefixime Oral Susp 100mg/5ml ➔ 1,800 Packs</div>
                            <div class="text-slate-600 text-[11px]">Routing: Guwahati Central C&F ➔ Dibrugarh Super Stockist</div>
                            <div class="text-blue-700 text-[10px] font-semibold">AI Model: IDSP Epidemiological Outbreak Predictor · Confidence: 91.2%</div>
                        </div>
                        <div class="flex items-center space-x-2">
                            <button onclick="approveIndent('indentCard-2', 'PO-DHN-9902', 'Dibrugarh Super Stockist')" class="px-4 py-2 bg-emerald-600 hover:bg-emerald-700 text-white font-bold rounded-xl text-xs transition shadow-sm">
                                Approve & Issue PO
                            </button>
                            <button onclick="rejectIndent('indentCard-2')" class="px-3 py-2 bg-white hover:bg-slate-100 text-rose-700 border border-slate-200 rounded-xl text-xs font-semibold transition">
                                Reject
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Tab 5: GxP Audit & Recall -->
            <div id="adminTab-audit" class="hidden space-y-4 text-xs max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-center justify-between">
                    <div>
                        <h4 class="text-sm font-bold text-slate-900">CDSCO / WHO GxP Audit Ledger & Emergency Batch Recall Control</h4>
                        <p class="text-slate-500">Cryptographically verifiable audit log of human approvals, batch movements, and emergency containment.</p>
                    </div>
                    <button onclick="triggerEmergencyRecallModal()" class="px-3.5 py-2 rounded-xl bg-rose-600 hover:bg-rose-700 text-white font-bold flex items-center gap-1.5 shadow-sm">
                        <i data-lucide="alert-octagon" class="w-3.5 h-3.5"></i>
                        <span>Initiate Batch Quarantine / Recall</span>
                    </button>
                </div>

                <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 space-y-2.5">
                    <div class="font-bold text-slate-800">Recent Immutable Audit Entries:</div>
                    <div class="font-mono text-[10px] space-y-1.5" id="auditLogList">
                        <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex justify-between text-slate-800 shadow-sm">
                            <span>[2026-11-23 02:44:12] AUTH_APPROVED: Indent #REC-401 ➔ Silchar (2,500 vials ASV) by admin@dhanuka.com</span>
                            <span class="text-blue-700 font-bold">SHA256: 8f4b...39a1</span>
                        </div>
                        <div class="p-2.5 bg-white rounded-lg border border-slate-200 flex justify-between text-slate-800 shadow-sm">
                            <span>[2026-11-23 02:38:05] FEFO_REBALANCE: Batch #ARB-204 (180 vials) Tezpur ➔ Silchar executed</span>
                            <span class="text-blue-700 font-bold">SHA256: d2e9...710c</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Modal Footer -->
            <div class="pt-3 border-t border-slate-100 flex justify-between items-center text-xs">
                <span class="text-slate-500 font-mono font-medium">Dhanuka MediFlow-NE Core Engine v1.2</span>
                <button onclick="closeAdminPanelModal()" class="px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-800 font-bold text-xs border border-slate-200 transition">
                    Close Command Console
                </button>
            </div>
        </div>
    </div>

    <!-- App Logic Script -->
    <script>
        // Smooth scroll helper
        function scrollToSection(id) {
            const el = document.getElementById(id);
            if (el) el.scrollIntoView({ behavior: 'smooth' });
        }

        // Initialize Lucide Icons
        lucide.createIcons();

        // 1. Initialize Leaflet Map (Light Mode Carto Positron Tiles)
        const map = L.map('supplyMap').setView([26.2006, 92.9376], 7);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
            attribution: '&copy; OpenStreetMap contributors &copy; CARTO',
            maxZoom: 14,
            minZoom: 6
        }).addTo(map);

        // Nodes data
        const supplyNodes = [
            { id: 'guwahati', name: 'Guwahati Central C&F Hub (Dhanuka Complex)', coords: [26.1856, 91.7454], type: 'central', status: 'optimal', leadTime: '0 Days (Hub)', runway: '45 Days' },
            { id: 'tezpur', name: 'Tezpur Staging Depot', coords: [26.6338, 92.8006], type: 'intermediate', status: 'optimal', leadTime: '2 - 3 Days', runway: '32 Days' },
            { id: 'dibrugarh', name: 'Dibrugarh Super Stockist (Upper Assam)', coords: [27.4728, 94.9120], type: 'stockist', status: 'warning', leadTime: '5 - 7 Days', runway: '18 Days' },
            { id: 'silchar', name: 'Silchar Buffer Depot (Barak Valley)', coords: [24.8333, 92.7789], type: 'stockist', status: 'critical', leadTime: '18 - 25 Days (Flood)', runway: '11.4 Days' },
            { id: 'shillong', name: 'Shillong Hill Warehouse', coords: [25.5788, 91.8933], type: 'stockist', status: 'optimal', leadTime: '3 - 4 Days', runway: '28 Days' },
            { id: 'aizawl', name: 'Aizawl Distribution Depot', coords: [23.7271, 92.7176], type: 'stockist', status: 'warning', leadTime: '12 - 16 Days', runway: '14 Days' },
            { id: 'dimapur', name: 'Dimapur / Kohima Node', coords: [25.9094, 93.7266], type: 'stockist', status: 'warning', leadTime: '7 - 10 Days', runway: '16 Days' },
            { id: 'agartala', name: 'Agartala Sub-Depot', coords: [23.8315, 91.2868], type: 'stockist', status: 'warning', leadTime: '14 - 18 Days', runway: '15 Days' }
        ];

        // Draw corridors
        const corridors = [
            { from: [26.1856, 91.7454], to: [26.6338, 92.8006], color: '#10b981', dash: '' }, // Guwahati -> Tezpur
            { from: [26.6338, 92.8006], to: [27.4728, 94.9120], color: '#f59e0b', dash: '5, 5' }, // Tezpur -> Dibrugarh
            { from: [26.1856, 91.7454], to: [25.5788, 91.8933], color: '#10b981', dash: '' }, // Guwahati -> Shillong
            { from: [25.5788, 91.8933], to: [24.8333, 92.7789], color: '#ef4444', dash: '6, 6' }, // Shillong -> Silchar (NH-6 Hazard)
            { from: [24.8333, 92.7789], to: [23.7271, 92.7176], color: '#f59e0b', dash: '5, 5' }, // Silchar -> Aizawl
            { from: [26.6338, 92.8006], to: [25.9094, 93.7266], color: '#f59e0b', dash: '5, 5' }, // Tezpur -> Dimapur
            { from: [24.8333, 92.7789], to: [23.8315, 91.2868], color: '#f59e0b', dash: '5, 5' }  // Silchar -> Agartala
        ];

        corridors.forEach(c => {
            L.polyline([c.from, c.to], { color: c.color, weight: 3.5, dashArray: c.dash, opacity: 0.9 }).addTo(map);
        });

        // Add Markers
        supplyNodes.forEach(node => {
            const color = node.status === 'optimal' ? '#10b981' : (node.status === 'warning' ? '#f59e0b' : '#ef4444');
            const radius = node.type === 'central' ? 10 : 7;

            const circle = L.circleMarker(node.coords, {
                radius: radius,
                fillColor: color,
                color: '#ffffff',
                weight: 2,
                opacity: 1,
                fillOpacity: 0.95
            }).addTo(map);

            circle.bindTooltip(`<b>${node.name}</b><br/>Lead Time: ${node.leadTime}<br/>Runway: ${node.runway}`, { className: 'bg-white text-slate-800 shadow-md border border-slate-200' });

            circle.on('click', () => {
                document.getElementById('selectedNodeTitle').innerText = node.name;
                document.getElementById('nodeLeadTime').innerText = node.leadTime;
                document.getElementById('nodeRunway').innerText = node.runway;
                const badge = document.getElementById('selectedNodeBadge');
                if (node.status === 'critical') {
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold';
                    badge.innerText = 'High Bottleneck Risk';
                } else if (node.status === 'warning') {
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-amber-50 text-amber-700 border border-amber-200 font-bold';
                    badge.innerText = 'Flood Warning';
                } else {
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold';
                    badge.innerText = 'Optimal Operations';
                }
            });
        });

        // 2. Initialize Chart.js Forecast (Light Theme)
        const ctx = document.getElementById('forecastChart').getContext('2d');
        const labels = ['W1 (Actual)', 'W2 (Actual)', 'W3 (Actual)', 'W4 (Actual)', 'W5 (P50)', 'W6 (P50)', 'W7 (Flood Peak)', 'W8 (P50)', 'W9 (P50)', 'W10 (P50)', 'W11 (P50)', 'W12 (P50)'];
        
        let historical = [2800, 3100, 2950, 3300, null, null, null, null, null, null, null, null];
        let p50 = [null, null, null, 3300, 3900, 4800, 6200, 5700, 4600, 3800, 3400, 3200];
        let p90 = [null, null, null, 3300, 4400, 5600, 7400, 6800, 5400, 4300, 3800, 3500];
        let p10 = [null, null, null, 3300, 3500, 4200, 5100, 4700, 3900, 3300, 3000, 2900];

        const forecastChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [
                    {
                        label: 'Historical Dispatches',
                        data: historical,
                        borderColor: '#64748b',
                        backgroundColor: '#64748b',
                        borderWidth: 2,
                        tension: 0.2
                    },
                    {
                        label: 'P50 Median Forecast',
                        data: p50,
                        borderColor: '#2563eb',
                        backgroundColor: '#2563eb',
                        borderWidth: 2.5,
                        tension: 0.3
                    },
                    {
                        label: 'P90 Upper Bound',
                        data: p90,
                        borderColor: 'rgba(37, 99, 235, 0.2)',
                        backgroundColor: 'rgba(37, 99, 235, 0.08)',
                        fill: '+1',
                        borderWidth: 1,
                        pointRadius: 0
                    },
                    {
                        label: 'P10 Lower Bound',
                        data: p10,
                        borderColor: 'rgba(37, 99, 235, 0.2)',
                        backgroundColor: 'transparent',
                        borderWidth: 1,
                        pointRadius: 0
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    x: {
                        grid: { color: '#f1f5f9' },
                        ticks: { color: '#475569', font: { size: 10, weight: '500' } }
                    },
                    y: {
                        grid: { color: '#f1f5f9' },
                        ticks: { color: '#475569', font: { size: 10, weight: '500' } }
                    }
                },
                plugins: {
                    legend: {
                        labels: { color: '#1e293b', font: { size: 10, weight: '600' } }
                    }
                }
            }
        });

        // Scenario updater
        function updateScenario() {
            const flood = parseInt(document.getElementById('floodSlider').value);
            const outbreak = parseInt(document.getElementById('outbreakSlider').value);
            const delay = parseInt(document.getElementById('delaySlider').value);

            document.getElementById('floodVal').innerText = `Level ${flood} (${flood >= 4 ? 'Severe Washouts' : 'Moderate Inundation'})`;
            document.getElementById('outbreakVal').innerText = `+${outbreak}% (${outbreak > 30 ? 'JE & Dengue Spike' : 'Seasonal Baseline'})`;
            document.getElementById('delayVal').innerText = `+${delay} Days`;

            const multiplier = 1 + (flood * 0.1) + (outbreak * 0.005);
            forecastChart.data.datasets[1].data[6] = Math.round(4800 * multiplier);
            forecastChart.data.datasets[2].data[6] = Math.round(5600 * multiplier * 1.15);
            forecastChart.update();
        }

        function triggerDemoPrepositioning() {
            document.getElementById('kpiInStock').innerText = '98.9%';
            document.getElementById('kpiAlerts').innerText = '0 (Secured)';
            alert('✓ Pre-Monsoon Pre-Positioning Buffer Activated!\n3,400 units dispatched to Silchar & Aizawl ahead of forecasted heavy monsoon spell.');
        }

        function dispatchEmergencyIndent() {
            document.getElementById('dispatchIndentBtn').disabled = true;
            document.getElementById('dispatchIndentBtn').innerText = 'Processing via Dhanuka ERP...';
            setTimeout(() => {
                document.getElementById('dispatchIndentBtn').classList.add('hidden');
                document.getElementById('dispatchSuccessMsg').classList.remove('hidden');
                document.getElementById('nodeRunway').innerText = '36.5 Days (Secured)';
                document.getElementById('nodeRunway').className = 'text-emerald-700 font-bold';
            }, 800);
        }

        function executeRebalance(btn, batchId) {
            btn.disabled = true;
            btn.innerText = 'Rebalanced ✓';
            btn.className = 'px-2.5 py-1 bg-emerald-600 text-white rounded-lg text-[11px] font-semibold';
            const kpi = document.getElementById('kpiRebalanced');
            kpi.innerText = '1,600 pk';
        }

        function sendChatMessage() {
            const input = document.getElementById('chatInput');
            const text = input.value.trim();
            if (!text) return;

            const chatWindow = document.getElementById('chatWindow');

            const userBubble = document.createElement('div');
            userBubble.className = 'flex items-start justify-end space-x-2';
            userBubble.innerHTML = `
                <div class="bg-emerald-600 text-white p-2.5 rounded-xl rounded-tr-none max-w-[85%] shadow-sm">
                    ${text}
                    <div class="text-[9px] text-emerald-100 mt-1 text-right">Just now · Chemist</div>
                </div>
            `;
            chatWindow.appendChild(userBubble);
            input.value = '';
            chatWindow.scrollTop = chatWindow.scrollHeight;

            setTimeout(() => {
                const botBubble = document.createElement('div');
                botBubble.className = 'flex items-start space-x-2';
                botBubble.innerHTML = `
                    <div class="w-6 h-6 rounded-full bg-emerald-600 flex items-center justify-center text-[10px] font-bold text-white">MB</div>
                    <div class="bg-white text-slate-800 p-2.5 rounded-xl rounded-tl-none max-w-[85%] border border-slate-200 shadow-sm">
                        ✓ Requisition logged into Dhanuka ERP! Stock allocated from nearest regional staging hub. Tracking ID: #TRK-9842.
                        <div class="text-[9px] text-slate-400 mt-1">Just now · MediFlow Bot</div>
                    </div>
                `;
                chatWindow.appendChild(botBubble);
                chatWindow.scrollTop = chatWindow.scrollHeight;
            }, 600);
        }

        function applyOptimizedPlan() {
            alert('✓ Google OR-Tools MILP optimization executed!\nRe-allocated 4,200 packs across 8 Northeast hubs, reducing stockout vulnerability by 86%.');
            document.getElementById('kpiInStock').innerText = '97.8%';
        }

        // Modal Controls
        function openTutorialModal() {
            document.getElementById('tutorialModal').classList.remove('hidden');
        }
        function closeTutorialModal() {
            document.getElementById('tutorialModal').classList.add('hidden');
        }

        let isAdminLoggedIn = false;
        function openAdminModal() {
            if (isAdminLoggedIn) {
                document.getElementById('adminPanelModal').classList.remove('hidden');
            } else {
                document.getElementById('adminLoginModal').classList.remove('hidden');
            }
        }
        function closeAdminLoginModal() {
            document.getElementById('adminLoginModal').classList.add('hidden');
            document.getElementById('loginErrorMsg').classList.add('hidden');
        }
        function closeAdminPanelModal() {
            document.getElementById('adminPanelModal').classList.add('hidden');
        }

        function fillDemoCredentials() {
            document.getElementById('adminEmailInput').value = 'admin@dhanuka.com';
            document.getElementById('adminPassInput').value = 'dhanuka2026';
        }

        function handleAdminLogin(e) {
            e.preventDefault();
            const email = document.getElementById('adminEmailInput').value.trim();
            const pass = document.getElementById('adminPassInput').value.trim();

            if (email === 'admin@dhanuka.com' && pass === 'dhanuka2026') {
                isAdminLoggedIn = true;
                closeAdminLoginModal();
                document.getElementById('adminHeaderLabel').innerText = 'Admin Console (Active)';
                document.getElementById('adminLoginHeaderBtn').className = 'px-3.5 py-1.5 rounded-lg bg-emerald-50 hover:bg-emerald-100 text-emerald-800 border border-emerald-300 text-xs font-semibold flex items-center space-x-1.5 transition';
                document.getElementById('adminPanelModal').classList.remove('hidden');
            } else {
                document.getElementById('loginErrorMsg').classList.remove('hidden');
            }
        }

        function handleAdminLogout() {
            isAdminLoggedIn = false;
            closeAdminPanelModal();
            document.getElementById('adminHeaderLabel').innerText = 'Admin Console (Login)';
            document.getElementById('adminLoginHeaderBtn').className = 'px-3.5 py-1.5 rounded-lg bg-purple-50 hover:bg-purple-100 text-purple-800 border border-purple-300 text-xs font-semibold flex items-center space-x-1.5 transition';
            alert('Admin logged out successfully.');
        }

        function switchAdminTab(tabName) {
            const tabs = ['corridors', 'skus', 'stockists', 'dispatches', 'audit'];
            tabs.forEach(t => {
                const btn = document.getElementById(`tabBtn-${t}`);
                const panel = document.getElementById(`adminTab-${t}`);
                if (btn && panel) {
                    if (t === tabName) {
                        panel.classList.remove('hidden');
                        btn.className = 'px-3.5 py-2 font-bold rounded-lg bg-purple-50 text-purple-800 border border-purple-200 flex items-center gap-1.5 transition';
                    } else {
                        panel.classList.add('hidden');
                        btn.className = 'px-3.5 py-2 font-medium rounded-lg text-slate-600 hover:text-slate-900 hover:bg-slate-100 flex items-center gap-1.5 transition';
                    }
                }
            });
            lucide.createIcons();
        }

        function toggleRouteStatus(route) {
            if (route === 'nh6') {
                const badge = document.getElementById('adminNH6Badge');
                if (badge.innerText.includes('Flood')) {
                    badge.innerText = 'Clear & Optimal';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold';
                    document.getElementById('adminNH6Days').innerText = '3 - 5 Days (Normal)';
                    document.getElementById('adminNH6Days').className = 'text-emerald-700 font-bold';
                } else {
                    badge.innerText = 'Flood Hazard Active';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-rose-50 text-rose-700 border border-rose-200 font-bold';
                    document.getElementById('adminNH6Days').innerText = '18 - 25 Days (+16d Delay)';
                    document.getElementById('adminNH6Days').className = 'text-rose-600 font-bold';
                }
            } else if (route === 'nh29') {
                const badge = document.getElementById('adminNH29Badge');
                if (badge.innerText.includes('Caution')) {
                    badge.innerText = 'Clear & Optimal';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-emerald-50 text-emerald-700 border border-emerald-200 font-bold';
                    document.getElementById('adminNH29Days').innerText = '4 - 6 Days (Normal)';
                    document.getElementById('adminNH29Days').className = 'text-emerald-700 font-bold';
                } else {
                    badge.innerText = 'Landslide Caution';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-amber-50 text-amber-700 border border-amber-200 font-bold';
                    document.getElementById('adminNH29Days').innerText = '7 - 10 Days (+4d Delay)';
                    document.getElementById('adminNH29Days').className = 'text-amber-700 font-bold';
                }
            }
        }

        function resetCorridorDefaults() {
            alert('✓ Telemetry reset: Default ASDMA monsoon baseline loaded.');
        }

        function triggerForceSyncAll() {
            alert('✓ Force Sync Ingestion Triggered! Ingested 48 stockist ledgers across Assam, Meghalaya, and Nagaland in 1.4s.');
        }

        let pendingIndents = 3;
        function approveIndent(cardId, poNumber, destination) {
            const card = document.getElementById(cardId);
            if (card) {
                card.innerHTML = `
                    <div class="p-3 bg-emerald-50 border border-emerald-200 rounded-xl text-emerald-800 w-full flex items-center justify-between">
                        <div>
                            <strong class="text-emerald-950">✓ Approved & Pushed to Dhanuka SAP ERP!</strong>
                            <div class="text-[11px] text-emerald-700 font-medium">Generated Purchase Order #${poNumber} for ${destination}. Dispatched to priority carrier.</div>
                        </div>
                        <span class="text-xs font-mono text-emerald-800 font-bold">PO_STATUS: ISSUED</span>
                    </div>
                `;
                pendingIndents--;
                document.getElementById('pendingIndentCountBadge').innerText = pendingIndents;
                const log = document.getElementById('auditLogList');
                if (log) {
                    const newLog = document.createElement('div');
                    newLog.className = 'p-2.5 bg-white rounded-lg border border-slate-200 flex justify-between text-slate-800 shadow-sm';
                    newLog.innerHTML = `<span>[Just now] AUTH_APPROVED: Indent #${poNumber} issued by admin@dhanuka.com</span><span class="text-blue-700 font-bold">SHA256: 7ca2...19df</span>`;
                    log.prepend(newLog);
                }
                document.getElementById('kpiInStock').innerText = '97.8%';
            }
        }

        function rejectIndent(cardId) {
            const card = document.getElementById(cardId);
            if (card) {
                card.remove();
                pendingIndents--;
                document.getElementById('pendingIndentCountBadge').innerText = pendingIndents;
            }
        }

        function triggerEmergencyRecallModal() {
            const batch = prompt('Enter Batch ID to initiate emergency multi-tier quarantine (e.g. ASV-882):', 'ASV-882');
            if (batch) {
                alert(`🚨 EMERGENCY BATCH QUARANTINE ISSUED FOR #${batch}!\n\n1. Instant quarantine broadcast sent to 48 stockists.\n2. Marg/Tally ERP billing locked for this batch.\n3. CDSCO quality alert recorded with SHA-256 cryptographic hash.`);
                const log = document.getElementById('auditLogList');
                if (log) {
                    const newLog = document.createElement('div');
                    newLog.className = 'p-2.5 bg-rose-50 rounded-lg border border-rose-200 flex justify-between text-rose-900 font-bold';
                    newLog.innerHTML = `<span>[Emergency Alert] BATCH_QUARANTINE: Batch #${batch} locked system-wide by admin@dhanuka.com</span><span class="text-rose-700">SHA256: b8e1...44a9</span>`;
                    log.prepend(newLog);
                }
            }
        }
    </script>
</body>
</html>
"""

with open("app/index.html", "w") as f:
    f.write(html_content)

print("Clean white background app with Landing Page created successfully.")
