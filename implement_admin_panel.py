import re

with open("app/index.html") as f:
    content = f.read()

# 1. New comprehensive Admin Modal
admin_panel_modal_new = """
    <!-- Admin Panel Full Modal (Unlocked after Login) -->
    <div id="adminPanelModal" class="hidden fixed inset-0 z-50 bg-black/90 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
        <div class="glass-panel bg-slate-900 border border-slate-700 rounded-2xl max-w-5xl w-full p-6 shadow-2xl space-y-5 text-slate-200 my-6">
            
            <!-- Modal Header -->
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 rounded-xl bg-purple-600/30 border border-purple-500/50 flex items-center justify-center text-purple-300">
                        <i data-lucide="shield-check" class="w-5 h-5 text-purple-400"></i>
                    </div>
                    <div>
                        <div class="flex items-center space-x-2">
                            <h2 class="text-base font-bold text-white">Dhanuka Central Admin Command Console</h2>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-mono">Role: Enterprise SCM Admin</span>
                        </div>
                        <p class="text-xs text-slate-400">Network Hazards, SKU Buffer Rules, ERP Gateways, Indent Approvals & GxP Audit Ledger</p>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <button onclick="handleAdminLogout()" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-rose-300 text-xs border border-slate-700 flex items-center gap-1.5 transition">
                        <i data-lucide="log-out" class="w-3.5 h-3.5"></i>
                        <span>Logout</span>
                    </button>
                    <button onclick="closeAdminPanelModal()" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>
            </div>

            <!-- Tab Navigation Bar -->
            <div class="flex items-center space-x-1 border-b border-slate-800 text-xs overflow-x-auto pb-1">
                <button onclick="switchAdminTab('corridors')" id="tabBtn-corridors" class="px-3.5 py-2 font-medium rounded-lg bg-purple-600/30 text-purple-200 border border-purple-500/40 flex items-center gap-1.5 transition">
                    <i data-lucide="truck" class="w-4 h-4"></i>
                    <span>Corridor Hazards & Routes</span>
                </button>
                <button onclick="switchAdminTab('skus')" id="tabBtn-skus" class="px-3.5 py-2 font-medium rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 flex items-center gap-1.5 transition">
                    <i data-lucide="package" class="w-4 h-4"></i>
                    <span>Master SKU & Buffer Policies</span>
                </button>
                <button onclick="switchAdminTab('stockists')" id="tabBtn-stockists" class="px-3.5 py-2 font-medium rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 flex items-center gap-1.5 transition">
                    <i data-lucide="database" class="w-4 h-4"></i>
                    <span>Stockist ERP Network</span>
                </button>
                <button onclick="switchAdminTab('dispatches')" id="tabBtn-dispatches" class="px-3.5 py-2 font-medium rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 flex items-center gap-1.5 transition">
                    <i data-lucide="check-circle" class="w-4 h-4"></i>
                    <span>AI Dispatch Approvals <span id="pendingIndentCountBadge" class="ml-1 px-1.5 py-0.2 rounded-full bg-cyan-950 text-cyan-300 border border-cyan-800 text-[10px]">3</span></span>
                </button>
                <button onclick="switchAdminTab('audit')" id="tabBtn-audit" class="px-3.5 py-2 font-medium rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 flex items-center gap-1.5 transition">
                    <i data-lucide="file-check" class="w-4 h-4"></i>
                    <span>GxP Audit & Batch Recall</span>
                </button>
            </div>

            <!-- Tab 1: Corridors & Hazards -->
            <div id="adminTab-corridors" class="space-y-4 text-xs max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="text-sm font-semibold text-white">Regional Transit Corridor Vulnerability Manager</h3>
                        <p class="text-slate-400">Override real-time environmental disruption telemetry to trigger automated network-wide replenishment recalculations.</p>
                    </div>
                    <button onclick="resetCorridorDefaults()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] border border-slate-700">
                        Reset Telemetry
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3.5">
                    <!-- Corridor 1: NH-6 -->
                    <div class="bg-slate-800/60 p-4 rounded-xl border border-slate-700/80 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-white text-sm">NH-6: Guwahati ➔ Shillong ➔ Silchar</div>
                                <div class="text-slate-400 text-[11px]">Barak Valley, Tripura & Mizoram Lifeline Corridor</div>
                            </div>
                            <span id="adminNH6Badge" class="text-[10px] px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold">Flood Hazard Active</span>
                        </div>
                        <div class="flex justify-between text-slate-300 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-rose-400 font-bold" id="adminNH6Days">18 - 25 Days (+16d Delay)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="toggleRouteStatus('nh6')" class="w-full py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-medium text-xs transition">
                                Toggle Road Status (Clear / Flood)
                            </button>
                        </div>
                    </div>

                    <!-- Corridor 2: NH-29 -->
                    <div class="bg-slate-800/60 p-4 rounded-xl border border-slate-700/80 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-white text-sm">NH-29: Tezpur ➔ Dimapur ➔ Kohima</div>
                                <div class="text-slate-400 text-[11px]">Nagaland & Manipur Mountain Transit Highway</div>
                            </div>
                            <span id="adminNH29Badge" class="text-[10px] px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold">Landslide Caution</span>
                        </div>
                        <div class="flex justify-between text-slate-300 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-amber-400 font-bold" id="adminNH29Days">7 - 10 Days (+4d Delay)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="toggleRouteStatus('nh29')" class="w-full py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-medium text-xs transition">
                                Toggle Road Status (Clear / Caution)
                            </button>
                        </div>
                    </div>

                    <!-- Corridor 3: NH-27 -->
                    <div class="bg-slate-800/60 p-4 rounded-xl border border-slate-700/80 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-white text-sm">NH-27: Guwahati ➔ Tezpur ➔ Dibrugarh</div>
                                <div class="text-slate-400 text-[11px]">East-West Four-Lane Arterial (Upper Assam)</div>
                            </div>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-bold">Clear & Optimal</span>
                        </div>
                        <div class="flex justify-between text-slate-300 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-emerald-400 font-bold">3 - 5 Days (Nominal)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="alert('NH-27 status updated: In-transit telemetry confirmed clear.')" class="w-full py-1.5 rounded-lg bg-slate-700 hover:bg-slate-600 text-slate-200 font-medium text-xs transition">
                                Run Diagnostics
                            </button>
                        </div>
                    </div>

                    <!-- Corridor 4: Brahmaputra Riverine / Island Routes -->
                    <div class="bg-slate-800/60 p-4 rounded-xl border border-slate-700/80 space-y-2.5">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="font-bold text-white text-sm">Brahmaputra Riverine Crossing (Majuli Hub)</div>
                                <div class="text-slate-400 text-[11px]">Ferry-Dependent Island Clinics & Riverine PHCs</div>
                            </div>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold">Ferry Suspended</span>
                        </div>
                        <div class="flex justify-between text-slate-300 text-[11px]">
                            <span>Lead-Time Impact:</span>
                            <span class="text-amber-400 font-bold">High Water Delays (+10d)</span>
                        </div>
                        <div class="flex items-center space-x-2 pt-1">
                            <button onclick="alert('Drone emergency corridor activated for Majuli riverine dispatch!')" class="w-full py-1.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-medium text-xs transition">
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
                        <h3 class="text-sm font-semibold text-white">Pharmaceutical Master SKU Catalog & Dynamic Buffer Rules</h3>
                        <p class="text-slate-400">Configure ABC-VED priorities, storage conditions, and seasonal pre-monsoon safety buffers.</p>
                    </div>
                    <button onclick="alert('New SKU wizard initialized! Ingesting barcode schema...')" class="px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-medium flex items-center gap-1.5">
                        <i data-lucide="plus-circle" class="w-3.5 h-3.5"></i>
                        <span>Add New SKU</span>
                    </button>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-left">
                        <thead>
                            <tr class="text-slate-400 border-b border-slate-800 text-[11px]">
                                <th class="pb-2">SKU Code / Description</th>
                                <th class="pb-2">ABC-VED Tag</th>
                                <th class="pb-2">Storage Spec</th>
                                <th class="pb-2">Standard Buffer</th>
                                <th class="pb-2">Monsoon Pre-Position Buffer</th>
                                <th class="pb-2 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800" id="skuMasterTable">
                            <tr class="hover:bg-slate-800/40">
                                <td class="py-2.5 font-medium text-white">
                                    #SKU-001 · Polyvalent Anti-Snake Venom (10ml)
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold text-[10px]">Vital (V)</span></td>
                                <td class="py-2.5 text-cyan-300 font-mono">2°C–8°C Cold Chain</td>
                                <td class="py-2.5 text-slate-300">21 Days</td>
                                <td class="py-2.5 text-emerald-400 font-bold">35 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated: 35 days enforced for Assam floods.')" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded text-[10px]">Edit Rule</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-800/40">
                                <td class="py-2.5 font-medium text-white">
                                    #SKU-002 · Human Regular Insulin 40IU/ml
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold text-[10px]">Vital (V)</span></td>
                                <td class="py-2.5 text-cyan-300 font-mono">2°C–8°C Cold Chain</td>
                                <td class="py-2.5 text-slate-300">21 Days</td>
                                <td class="py-2.5 text-emerald-400 font-bold">28 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated.')" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded text-[10px]">Edit Rule</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-800/40">
                                <td class="py-2.5 font-medium text-white">
                                    #SKU-003 · Cefixime Oral Susp 100mg/5ml
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-blue-950 text-blue-300 border border-blue-800 font-bold text-[10px]">Essential (E)</span></td>
                                <td class="py-2.5 text-slate-400">Room Temp (&lt; 25°C)</td>
                                <td class="py-2.5 text-slate-300">14 Days</td>
                                <td class="py-2.5 text-emerald-400 font-bold">28 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated.')" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded text-[10px]">Edit Rule</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-800/40">
                                <td class="py-2.5 font-medium text-white">
                                    #SKU-004 · Paracetamol IV Infusion 100ml
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-blue-950 text-blue-300 border border-blue-800 font-bold text-[10px]">Essential (E)</span></td>
                                <td class="py-2.5 text-slate-400">Room Temp (&lt; 25°C)</td>
                                <td class="py-2.5 text-slate-300">15 Days</td>
                                <td class="py-2.5 text-emerald-400 font-bold">30 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated.')" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded text-[10px]">Edit Rule</button>
                                </td>
                            </tr>
                            <tr class="hover:bg-slate-800/40">
                                <td class="py-2.5 font-medium text-white">
                                    #SKU-005 · Rabies Antiserum 1000IU
                                </td>
                                <td class="py-2.5"><span class="px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold text-[10px]">Vital (V)</span></td>
                                <td class="py-2.5 text-cyan-300 font-mono">2°C–8°C Cold Chain</td>
                                <td class="py-2.5 text-slate-300">21 Days</td>
                                <td class="py-2.5 text-emerald-400 font-bold">35 Days Buffer</td>
                                <td class="py-2.5 text-right">
                                    <button onclick="alert('Buffer policy updated.')" class="px-2 py-1 bg-slate-700 hover:bg-slate-600 text-slate-200 rounded text-[10px]">Edit Rule</button>
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
                        <h3 class="text-sm font-semibold text-white">Connected Stockist ERP & Ingestion Network (48 Active Nodes)</h3>
                        <p class="text-slate-400">Live heartbeat monitoring of automated data pipelines across Marg ERP, Tally Prime, and Busy installations.</p>
                    </div>
                    <button onclick="triggerForceSyncAll()" class="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-medium flex items-center gap-1.5">
                        <i data-lucide="refresh-cw" class="w-3.5 h-3.5"></i>
                        <span>Force Sync All Nodes</span>
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/80 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-white">Guwahati Central C&F</span>
                            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        </div>
                        <div class="text-[11px] text-slate-400">Dhanuka Enterprise Core (SAP)</div>
                        <div class="text-[10px] text-emerald-400 font-mono">Sync: 100% · Latency 140ms</div>
                    </div>

                    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/80 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-white">Dibrugarh Super Stockist</span>
                            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        </div>
                        <div class="text-[11px] text-slate-400">Upper Assam Agency (Marg ERP)</div>
                        <div class="text-[10px] text-emerald-400 font-mono">Sync: 12 min ago · 410 SKUs</div>
                    </div>

                    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/80 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-white">Silchar Buffer Depot</span>
                            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        </div>
                        <div class="text-[11px] text-slate-400">Barak Medicos (Tally Prime)</div>
                        <div class="text-[10px] text-emerald-400 font-mono">Sync: 24 min ago · 380 SKUs</div>
                    </div>

                    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/80 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-white">Tezpur Regional Wholesaler</span>
                            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        </div>
                        <div class="text-[11px] text-slate-400">Brahmaputra Pharma (Busy 21)</div>
                        <div class="text-[10px] text-emerald-400 font-mono">Sync: 45 min ago · 290 SKUs</div>
                    </div>

                    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/80 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-white">Shillong Hill Warehouse</span>
                            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        </div>
                        <div class="text-[11px] text-slate-400">Khasi Pharma Dist (Marg ERP)</div>
                        <div class="text-[10px] text-emerald-400 font-mono">Sync: 1 hr ago · 215 SKUs</div>
                    </div>

                    <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/80 space-y-1.5">
                        <div class="flex justify-between items-center">
                            <span class="font-bold text-white">Aizawl Distribution Depot</span>
                            <span class="w-2 h-2 rounded-full bg-emerald-400"></span>
                        </div>
                        <div class="text-[11px] text-slate-400">Mizoram Healthcare (Tally Prime)</div>
                        <div class="text-[10px] text-emerald-400 font-mono">Sync: 8 min ago · 185 SKUs</div>
                    </div>
                </div>

                <div class="bg-slate-800/40 p-3 rounded-lg border border-slate-700/60 text-slate-400 text-[11px] flex justify-between items-center">
                    <span>Zero-Footprint Sync Agent: Compatible with Marg ERP 9.0+, Tally Prime Release 2.0+, and Busy 18/21.</span>
                    <span class="text-cyan-400 font-mono">Total Monitored Ledger Rows: 1,480,240</span>
                </div>
            </div>

            <!-- Tab 4: AI Dispatch Approvals -->
            <div id="adminTab-dispatches" class="hidden space-y-4 text-xs max-h-[60vh] overflow-y-auto pr-2">
                <div class="flex items-center justify-between">
                    <div>
                        <h3 class="text-sm font-semibold text-white">Human-in-the-Loop AI Dispatch & Pre-Positioning Authorization Queue</h3>
                        <p class="text-slate-400">Review, modify, and authorize algorithmic indents before PO creation in Dhanuka SAP core.</p>
                    </div>
                    <span class="text-xs text-amber-300 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-800 font-mono">3 Indents Awaiting Approval</span>
                </div>

                <div class="space-y-3" id="indentCardsContainer">
                    <!-- Indent 1 -->
                    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/80 flex flex-wrap items-center justify-between gap-4" id="indentCard-1">
                        <div class="space-y-1 max-w-md">
                            <div class="flex items-center space-x-2">
                                <span class="text-xs font-bold text-white">Indent #REC-401</span>
                                <span class="px-2 py-0.2 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold text-[10px]">High Urgency (Pre-Flood)</span>
                            </div>
                            <div class="text-slate-300 font-medium">Polyvalent Anti-Snake Venom (10ml) ➔ 2,500 Vials</div>
                            <div class="text-slate-400 text-[11px]">Routing: Guwahati Central C&F ➔ Silchar Buffer Depot (Barak Valley)</div>
                            <div class="text-cyan-400 text-[10px]">AI Model: TFT Quantile P90 Surge · Confidence: 94.6% · Hazard: NH-6 Washout Risk</div>
                        </div>
                        <div class="flex items-center space-x-2">
                            <button onclick="approveIndent('indentCard-1', 'PO-DHN-9901', 'Silchar Buffer Depot')" class="px-4 py-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-semibold rounded-lg text-xs transition shadow-md shadow-emerald-600/30">
                                Approve & Issue PO
                            </button>
                            <button onclick="rejectIndent('indentCard-1')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700 rounded-lg text-xs transition">
                                Reject
                            </button>
                        </div>
                    </div>

                    <!-- Indent 2 -->
                    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/80 flex flex-wrap items-center justify-between gap-4" id="indentCard-2">
                        <div class="space-y-1 max-w-md">
                            <div class="flex items-center space-x-2">
                                <span class="text-xs font-bold text-white">Indent #REC-402</span>
                                <span class="px-2 py-0.2 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold text-[10px]">Seasonal Spurt</span>
                            </div>
                            <div class="text-slate-300 font-medium">Cefixime Oral Susp 100mg/5ml ➔ 1,800 Packs</div>
                            <div class="text-slate-400 text-[11px]">Routing: Guwahati Central C&F ➔ Dibrugarh Super Stockist</div>
                            <div class="text-cyan-400 text-[10px]">AI Model: IDSP Epidemiological Outbreak Predictor · Confidence: 91.2%</div>
                        </div>
                        <div class="flex items-center space-x-2">
                            <button onclick="approveIndent('indentCard-2', 'PO-DHN-9902', 'Dibrugarh Super Stockist')" class="px-4 py-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-semibold rounded-lg text-xs transition shadow-md shadow-emerald-600/30">
                                Approve & Issue PO
                            </button>
                            <button onclick="rejectIndent('indentCard-2')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700 rounded-lg text-xs transition">
                                Reject
                            </button>
                        </div>
                    </div>

                    <!-- Indent 3 -->
                    <div class="bg-slate-800/70 p-4 rounded-xl border border-slate-700/80 flex flex-wrap items-center justify-between gap-4" id="indentCard-3">
                        <div class="space-y-1 max-w-md">
                            <div class="flex items-center space-x-2">
                                <span class="text-xs font-bold text-white">Indent #REC-403</span>
                                <span class="px-2 py-0.2 rounded bg-blue-950 text-blue-300 border border-blue-800 font-bold text-[10px]">Hill Buffer</span>
                            </div>
                            <div class="text-slate-300 font-medium">Human Regular Insulin 40IU/ml ➔ 450 Vials (Cold Chain)</div>
                            <div class="text-slate-400 text-[11px]">Routing: Guwahati Central C&F ➔ Aizawl Distribution Depot</div>
                            <div class="text-cyan-400 text-[10px]">AI Model: MEIO Stochastic Lead-Time Optimizer · Confidence: 88.5%</div>
                        </div>
                        <div class="flex items-center space-x-2">
                            <button onclick="approveIndent('indentCard-3', 'PO-DHN-9903', 'Aizawl Depot')" class="px-4 py-2 bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-semibold rounded-lg text-xs transition shadow-md shadow-emerald-600/30">
                                Approve & Issue PO
                            </button>
                            <button onclick="rejectIndent('indentCard-3')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-rose-300 border border-slate-700 rounded-lg text-xs transition">
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
                        <h3 class="text-sm font-semibold text-white">CDSCO / WHO GxP Audit Ledger & Emergency Batch Recall Control</h3>
                        <p class="text-slate-400">Cryptographically verifiable audit log of human approvals, batch movements, and emergency containment.</p>
                    </div>
                    <button onclick="triggerEmergencyRecallModal()" class="px-3 py-1.5 rounded-lg bg-rose-600 hover:bg-rose-500 text-white font-medium flex items-center gap-1.5">
                        <i data-lucide="alert-octagon" class="w-3.5 h-3.5"></i>
                        <span>Initiate Batch Quarantine / Recall</span>
                    </button>
                </div>

                <div class="bg-slate-800/60 p-3.5 rounded-xl border border-slate-700/80 space-y-2">
                    <div class="font-semibold text-slate-200">Recent Immutable Audit Entries:</div>
                    <div class="font-mono text-[10px] space-y-1.5" id="auditLogList">
                        <div class="p-2 bg-slate-900 rounded border border-slate-800 flex justify-between text-slate-300">
                            <span>[2026-11-23 02:44:12] AUTH_APPROVED: Indent #REC-401 ➔ Silchar (2,500 vials ASV) by admin@dhanuka.com</span>
                            <span class="text-cyan-400">SHA256: 8f4b...39a1</span>
                        </div>
                        <div class="p-2 bg-slate-900 rounded border border-slate-800 flex justify-between text-slate-300">
                            <span>[2026-11-23 02:38:05] FEFO_REBALANCE: Batch #ARB-204 (180 vials) Tezpur ➔ Silchar executed</span>
                            <span class="text-cyan-400">SHA256: d2e9...710c</span>
                        </div>
                        <div class="p-2 bg-slate-900 rounded border border-slate-800 flex justify-between text-slate-300">
                            <span>[2026-11-23 02:20:41] TELEMETRY_OVERRIDE: NH-6 Flood Hazard Index updated to Level 4 (ASDMA sync)</span>
                            <span class="text-cyan-400">SHA256: a19f...bb42</span>
                        </div>
                        <div class="p-2 bg-slate-900 rounded border border-slate-800 flex justify-between text-slate-300">
                            <span>[2026-11-23 02:05:18] ERP_INGEST_SYNC: Dibrugarh Marg ERP daily ledger ingested (410 SKUs, 0 errors)</span>
                            <span class="text-cyan-400">SHA256: f70a...19e8</span>
                        </div>
                    </div>
                </div>

                <div class="p-3 bg-purple-950/30 rounded-xl border border-purple-800/50 text-[11px] text-purple-200 flex justify-between items-center">
                    <span>Statutory Compliance: CDSCO Good Distribution Practices (GDP) · WHO TRS 957 Annex 5 · DPDP Act 2023 domestic cloud storage.</span>
                    <button onclick="alert('Audit compliance certificate exported in CSV/PDF format.')" class="px-2.5 py-1 bg-purple-800/60 hover:bg-purple-700 text-white rounded font-medium text-[10px]">
                        Export Audit Certificate
                    </button>
                </div>
            </div>

            <!-- Modal Footer -->
            <div class="pt-3 border-t border-slate-800 flex justify-between items-center text-xs">
                <span class="text-slate-500 font-mono">Dhanuka MediFlow-NE Core Engine v1.2</span>
                <button onclick="closeAdminPanelModal()" class="px-4 py-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-white font-semibold text-xs border border-slate-700 transition">
                    Close Command Console
                </button>
            </div>
        </div>
    </div>
"""

# Replace old adminPanelModal
pattern = r'<!-- Admin Panel Full Modal \(Unlocked after Login\) -->[\s\S]*?</div>\s*</div>\s*</div>'
if re.search(pattern, content):
    content = re.sub(pattern, admin_panel_modal_new, content)
    print("Replaced existing adminPanelModal via regex.")
else:
    # Alternative replace
    pos = content.find('id="adminPanelModal"')
    if pos != -1:
        # Find the start comment
        start_comment = content.rfind('<!-- Admin Panel Full Modal', 0, pos)
        # Find closing of this modal
        end_div = content.find('<!-- App Logic Script -->', pos)
        if start_comment != -1 and end_div != -1:
            content = content[:start_comment] + admin_panel_modal_new + "\n" + content[end_div:]
            print("Replaced adminPanelModal via slice.")
        else:
            print("Could not slice cleanly.")

# 2. Add JavaScript helper functions for Admin tabs & actions
js_tabs_code = """
        // Admin Tab Switching Logic
        function switchAdminTab(tabName) {
            const tabs = ['corridors', 'skus', 'stockists', 'dispatches', 'audit'];
            tabs.forEach(t => {
                const btn = document.getElementById(`tabBtn-${t}`);
                const panel = document.getElementById(`adminTab-${t}`);
                if (btn && panel) {
                    if (t === tabName) {
                        panel.classList.remove('hidden');
                        btn.className = 'px-3.5 py-2 font-medium rounded-lg bg-purple-600/30 text-purple-200 border border-purple-500/40 flex items-center gap-1.5 transition';
                    } else {
                        panel.classList.add('hidden');
                        btn.className = 'px-3.5 py-2 font-medium rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 flex items-center gap-1.5 transition';
                    }
                }
            });
            lucide.createIcons();
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
                    <div class="p-3 bg-emerald-950/50 border border-emerald-800/80 rounded-xl text-emerald-200 w-full flex items-center justify-between">
                        <div>
                            <strong class="text-white">✓ Approved & Pushed to Dhanuka SAP ERP!</strong>
                            <div class="text-[11px] text-emerald-300">Generated Purchase Order #${poNumber} for ${destination}. Dispatched to priority carrier.</div>
                        </div>
                        <span class="text-xs font-mono text-emerald-400">PO_STATUS: ISSUED</span>
                    </div>
                `;
                pendingIndents--;
                document.getElementById('pendingIndentCountBadge').innerText = pendingIndents;
                // Add to audit log
                const log = document.getElementById('auditLogList');
                if (log) {
                    const newLog = document.createElement('div');
                    newLog.className = 'p-2 bg-slate-900 rounded border border-slate-800 flex justify-between text-slate-300';
                    newLog.innerHTML = `<span>[Just now] AUTH_APPROVED: Indent #${poNumber} issued by admin@dhanuka.com</span><span class="text-cyan-400">SHA256: 7ca2...19df</span>`;
                    log.prepend(newLog);
                }
                // Update KPI
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
                    newLog.className = 'p-2 bg-rose-950/60 rounded border border-rose-800 flex justify-between text-rose-200';
                    newLog.innerHTML = `<span>[Emergency Alert] BATCH_QUARANTINE: Batch #${batch} locked system-wide by admin@dhanuka.com</span><span class="text-rose-400">SHA256: b8e1...44a9</span>`;
                    log.prepend(newLog);
                }
            }
        }
"""

content = content.replace("// Tutorial Modal Handlers", js_tabs_code + "\n        // Tutorial Modal Handlers")

with open("app/index.html", "w") as f:
    f.write(content)

print("Comprehensive Admin Panel implementation complete in app/index.html.")
