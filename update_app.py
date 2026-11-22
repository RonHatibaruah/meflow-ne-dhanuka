with open("app/index.html") as f:
    html = f.read()

# Let's inspect the header section to insert the Tutorial button and Admin button
header_buttons_old = """            <button onclick="triggerDemoPrepositioning()" class="px-3.5 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold shadow-md shadow-blue-600/30 flex items-center space-x-1.5 transition">
                <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                <span>Simulate Pre-Monsoon Pre-Positioning</span>
            </button>
            <a href="../NESFIC_I_09_Dhanuka_Proposal_PoW.pdf" target="_blank" class="px-3.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600 text-xs font-medium flex items-center space-x-1.5 transition">
                <i data-lucide="file-text" class="w-3.5 h-3.5 text-cyan-400"></i>
                <span>Proposal PDF</span>
            </a>"""

header_buttons_new = """            <button onclick="openTutorialModal()" class="px-3.5 py-1.5 rounded-lg bg-gradient-to-r from-amber-500/20 to-orange-500/20 hover:from-amber-500/30 hover:to-orange-500/30 text-amber-300 border border-amber-500/40 text-xs font-semibold flex items-center space-x-1.5 transition shadow-sm">
                <i data-lucide="help-circle" class="w-3.5 h-3.5 text-amber-400"></i>
                <span>Tutorial & Guide</span>
            </button>
            <button id="adminLoginHeaderBtn" onclick="openAdminModal()" class="px-3.5 py-1.5 rounded-lg bg-purple-600/30 hover:bg-purple-600/50 text-purple-200 border border-purple-500/50 text-xs font-semibold flex items-center space-x-1.5 transition">
                <i data-lucide="lock" class="w-3.5 h-3.5 text-purple-400"></i>
                <span id="adminHeaderLabel">Admin Panel (Login)</span>
            </button>
            <button onclick="triggerDemoPrepositioning()" class="px-3.5 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white text-xs font-semibold shadow-md shadow-blue-600/30 flex items-center space-x-1.5 transition">
                <i data-lucide="zap" class="w-3.5 h-3.5"></i>
                <span>Pre-Position Buffer</span>
            </button>
            <a href="NESFIC_I_09_Dhanuka_Proposal_PoW.pdf" target="_blank" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-600 text-xs font-medium flex items-center space-x-1.5 transition">
                <i data-lucide="file-text" class="w-3.5 h-3.5 text-cyan-400"></i>
                <span>PoW PDF</span>
            </a>"""

html = html.replace(header_buttons_old, header_buttons_new)

# Add Modals before </body>
modals_html = """
    <!-- Tutorial / Walkthrough Modal -->
    <div id="tutorialModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4 overflow-y-auto">
        <div class="glass-panel bg-slate-900 border border-slate-700 rounded-2xl max-w-3xl w-full p-6 shadow-2xl space-y-5 text-slate-200 my-8">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-3">
                    <div class="w-9 h-9 rounded-xl bg-amber-500/20 border border-amber-500/40 flex items-center justify-center text-amber-400">
                        <i data-lucide="book-open" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <h2 class="text-base font-bold text-white">MediFlow-NE: Interactive System Tutorial & User Guide</h2>
                        <p class="text-xs text-slate-400">Understanding the AI Supply Chain Platform for G.R. Dhanuka Group (NESFIC-I-09)</p>
                    </div>
                </div>
                <button onclick="closeTutorialModal()" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800">
                    <i data-lucide="x" class="w-5 h-5"></i>
                </button>
            </div>

            <!-- Tutorial Content -->
            <div class="space-y-4 text-xs max-h-[65vh] overflow-y-auto pr-2">
                <div class="bg-blue-950/40 border border-blue-800/60 p-3.5 rounded-xl text-blue-200 leading-relaxed">
                    <strong class="text-white flex items-center gap-1.5 mb-1">
                        <i data-lucide="info" class="w-4 h-4 text-cyan-400"></i>
                        The Regional Problem (NESFIC-I-09):
                    </strong>
                    Northeast India faces severe logistics bottlenecks due to seasonal Brahmaputra floods and landslides cutting key highway corridors (NH-6 to Barak Valley, NH-29 to Nagaland). Central warehouses in Guwahati lack visibility into peripheral chemists, causing <strong>25–34% stockouts of life-saving medicines</strong> during monsoons, while urban stockists face <strong>6–9% near-expiry wastage</strong>.
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                    <div class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/80 space-y-1.5">
                        <div class="font-bold text-cyan-300 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800 flex items-center justify-center text-[10px]">1</span>
                            Interactive GIS Logistics Radar
                        </div>
                        <p class="text-slate-400">Explore the interactive map of Northeast India. Click any hub (Guwahati, Silchar, Dibrugarh, Tezpur) to inspect lead-time variations, live flood hazard warnings along NH-6, and stock runway for vital medicines.</p>
                    </div>

                    <div class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/80 space-y-1.5">
                        <div class="font-bold text-cyan-300 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800 flex items-center justify-center text-[10px]">2</span>
                            AI Forecast & Scenario Studio
                        </div>
                        <p class="text-slate-400">Powered by Temporal Fusion Transformers (TFT). Adjust the <strong>Monsoon Severity</strong>, <strong>Epidemic Outbreak</strong>, and <strong>Transit Delay</strong> sliders to watch the demand forecast curve dynamically adapt in real-time.</p>
                    </div>

                    <div class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/80 space-y-1.5">
                        <div class="font-bold text-cyan-300 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800 flex items-center justify-center text-[10px]">3</span>
                            FEFO Expiry Arbitrage Matrix
                        </div>
                        <p class="text-slate-400">The platform automatically detects slow-moving batches nearing 6 months of expiry. Click <strong>"Rebalance"</strong> in the table to dynamically simulate transferring them to high-velocity emergency wards.</p>
                    </div>

                    <div class="p-3.5 rounded-xl bg-slate-800/60 border border-slate-700/80 space-y-1.5">
                        <div class="font-bold text-cyan-300 flex items-center gap-1.5">
                            <span class="w-5 h-5 rounded-full bg-cyan-950 text-cyan-400 border border-cyan-800 flex items-center justify-center text-[10px]">4</span>
                            Rural Chemist WhatsApp Bot
                        </div>
                        <p class="text-slate-400">Type a test message (e.g., <em>"Stock Cefixime: 5 packs left"</em>) in the mobile chat panel to experience how rural pharmacies with spotty 2G internet can log stock and confirm emergency replenishments in under 30 seconds.</p>
                    </div>
                </div>

                <div class="p-3.5 rounded-xl bg-purple-950/30 border border-purple-800/60 space-y-1.5">
                    <div class="font-bold text-purple-300 flex items-center gap-1.5">
                        <span class="w-5 h-5 rounded-full bg-purple-900 text-purple-300 border border-purple-700 flex items-center justify-center text-[10px]">5</span>
                        Admin Command & Control Center
                    </div>
                    <p class="text-slate-300">Click <strong>"Admin Panel (Login)"</strong> in the top header. Use demo credentials (<code>admin@dhanuka.com</code> / <code>dhanuka2026</code>) to unlock route hazard management, buffer rule tuning, stockist ERP sync health, and GxP audit logs.</p>
                </div>
            </div>

            <div class="pt-3 border-t border-slate-800 flex justify-between items-center text-xs">
                <span class="text-slate-500">NESFIC 2026 | Sponsoring Partner: G.R. Dhanuka Group</span>
                <button onclick="closeTutorialModal()" class="px-4 py-2 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-semibold transition">
                    Got it, Let's Explore!
                </button>
            </div>
        </div>
    </div>

    <!-- Admin Login Modal -->
    <div id="adminLoginModal" class="hidden fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
        <div class="glass-panel bg-slate-900 border border-slate-700 rounded-2xl max-w-md w-full p-6 shadow-2xl space-y-4 text-slate-200">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2.5">
                    <div class="w-8 h-8 rounded-lg bg-purple-600/30 border border-purple-500/50 flex items-center justify-center text-purple-300">
                        <i data-lucide="shield" class="w-4 h-4"></i>
                    </div>
                    <div>
                        <h2 class="text-sm font-bold text-white">Dhanuka Logistics Admin Login</h2>
                        <p class="text-[11px] text-slate-400">Secure Access to MediFlow-NE Command Console</p>
                    </div>
                </div>
                <button onclick="closeAdminLoginModal()" class="text-slate-400 hover:text-white p-1 rounded-lg">
                    <i data-lucide="x" class="w-4 h-4"></i>
                </button>
            </div>

            <!-- Demo Credentials Banner -->
            <div class="bg-purple-950/40 border border-purple-800/60 p-3 rounded-xl text-xs space-y-1">
                <div class="flex justify-between items-center">
                    <span class="text-purple-300 font-semibold">Demo Admin Credentials:</span>
                    <button onclick="fillDemoCredentials()" class="text-[10px] bg-purple-800/80 hover:bg-purple-700 text-purple-200 px-2 py-0.5 rounded font-mono transition">
                        ⚡ Quick Fill
                    </button>
                </div>
                <div class="text-[11px] text-slate-300 font-mono">
                    User: <strong class="text-white">admin@dhanuka.com</strong><br/>
                    Pass: <strong class="text-white">dhanuka2026</strong>
                </div>
            </div>

            <form onsubmit="handleAdminLogin(event)" class="space-y-3 text-xs">
                <div>
                    <label class="block text-slate-300 mb-1 font-medium">Username / Work Email</label>
                    <input type="text" id="adminEmailInput" required placeholder="admin@dhanuka.com" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-white focus:outline-none focus:border-purple-400">
                </div>
                <div>
                    <label class="block text-slate-300 mb-1 font-medium">Password</label>
                    <input type="password" id="adminPassInput" required placeholder="••••••••••••" class="w-full bg-slate-800 border border-slate-700 rounded-lg px-3 py-2 text-white focus:outline-none focus:border-purple-400">
                </div>
                <div id="loginErrorMsg" class="hidden text-rose-400 text-[11px] font-medium">
                    Invalid credentials. Please use the demo credentials above.
                </div>
                <button type="submit" class="w-full py-2.5 rounded-lg bg-gradient-to-r from-purple-600 to-indigo-600 hover:from-purple-500 hover:to-indigo-500 text-white font-semibold text-xs shadow-lg shadow-purple-600/30 transition">
                    Sign In to Admin Console
                </button>
            </form>
        </div>
    </div>

    <!-- Admin Panel Full Modal (Unlocked after Login) -->
    <div id="adminPanelModal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-4 overflow-y-auto">
        <div class="glass-panel bg-slate-900 border border-slate-700 rounded-2xl max-w-4xl w-full p-6 shadow-2xl space-y-5 text-slate-200 my-6">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-3">
                    <div class="w-9 h-9 rounded-xl bg-purple-600/30 border border-purple-500/50 flex items-center justify-center text-purple-300">
                        <i data-lucide="sliders" class="w-5 h-5"></i>
                    </div>
                    <div>
                        <h2 class="text-base font-bold text-white flex items-center gap-2">
                            <span>Dhanuka Central Admin Command Console</span>
                            <span class="text-[10px] px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-mono">Authenticated</span>
                        </h2>
                        <p class="text-xs text-slate-400">Network Hazard Controls, SKU Buffer Rules & GxP Compliance</p>
                    </div>
                </div>
                <div class="flex items-center space-x-2">
                    <button onclick="handleAdminLogout()" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-rose-300 text-xs border border-slate-700 flex items-center gap-1">
                        <i data-lucide="log-out" class="w-3.5 h-3.5"></i>
                        <span>Logout</span>
                    </button>
                    <button onclick="closeAdminPanelModal()" class="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800">
                        <i data-lucide="x" class="w-5 h-5"></i>
                    </button>
                </div>
            </div>

            <!-- Admin Tabs Content -->
            <div class="space-y-4 text-xs max-h-[65vh] overflow-y-auto pr-2">
                <!-- Tab 1: Corridor Hazard & Transit Rules -->
                <div class="bg-slate-800/60 p-4 rounded-xl border border-slate-700/80 space-y-3">
                    <h3 class="text-sm font-semibold text-white flex items-center gap-1.5">
                        <i data-lucide="truck" class="w-4 h-4 text-cyan-400"></i>
                        <span>Transit Corridor Hazard Overrides</span>
                    </h3>
                    <p class="text-slate-400">Dynamically update weather risk status and transit multiplier for key supply routes:</p>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
                        <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-700/60 flex items-center justify-between">
                            <div>
                                <div class="font-semibold text-white">NH-6 (Guwahati -> Meghalaya -> Silchar)</div>
                                <div class="text-[11px] text-slate-400">Barak Valley & Mizoram Lifeline</div>
                            </div>
                            <div class="flex items-center space-x-2">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold" id="nh6StatusBadge">Flood Active</span>
                                <button onclick="toggleRouteStatus('nh6')" class="px-2 py-1 rounded bg-slate-700 hover:bg-slate-600 text-white text-[11px]">
                                    Toggle
                                </button>
                            </div>
                        </div>

                        <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-700/60 flex items-center justify-between">
                            <div>
                                <div class="font-semibold text-white">NH-29 (Tezpur -> Dimapur / Kohima)</div>
                                <div class="text-[11px] text-slate-400">Nagaland & Manipur Transit</div>
                            </div>
                            <div class="flex items-center space-x-2">
                                <span class="text-[10px] px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold" id="nh29StatusBadge">Caution</span>
                                <button onclick="toggleRouteStatus('nh29')" class="px-2 py-1 rounded bg-slate-700 hover:bg-slate-600 text-white text-[11px]">
                                    Toggle
                                </button>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Tab 2: SKU Safety Buffer Tuning -->
                <div class="bg-slate-800/60 p-4 rounded-xl border border-slate-700/80 space-y-3">
                    <h3 class="text-sm font-semibold text-white flex items-center gap-1.5">
                        <i data-lucide="package" class="w-4 h-4 text-emerald-400"></i>
                        <span>SKU Buffer Safety Stock Rules</span>
                    </h3>
                    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
                        <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-700/60 space-y-1">
                            <span class="text-slate-400">Vital & Life-Saving (Antivenom)</span>
                            <div class="text-lg font-bold text-cyan-300">35 Days Buffer</div>
                            <div class="text-[10px] text-emerald-400">Pre-monsoon Pre-position active</div>
                        </div>
                        <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-700/60 space-y-1">
                            <span class="text-slate-400">Cold-Chain Biologics (Insulin)</span>
                            <div class="text-lg font-bold text-cyan-300">28 Days Buffer</div>
                            <div class="text-[10px] text-slate-400">2°C–8°C Logger verified</div>
                        </div>
                        <div class="bg-slate-900/80 p-3 rounded-lg border border-slate-700/60 space-y-1">
                            <span class="text-slate-400">General Formulations</span>
                            <div class="text-lg font-bold text-cyan-300">18 Days Buffer</div>
                            <div class="text-[10px] text-slate-400">Standard lead-time</div>
                        </div>
                    </div>
                </div>

                <!-- Tab 3: Connected ERPs & GxP Audit -->
                <div class="bg-slate-800/60 p-4 rounded-xl border border-slate-700/80 space-y-3">
                    <h3 class="text-sm font-semibold text-white flex items-center gap-1.5">
                        <i data-lucide="database" class="w-4 h-4 text-purple-400"></i>
                        <span>Stockist ERP Gateway Health & GxP Audit Trail</span>
                    </h3>
                    <div class="space-y-2">
                        <div class="flex justify-between items-center text-xs p-2 bg-slate-900/80 rounded border border-slate-800">
                            <span>Guwahati Central SAP C&F Gateway</span>
                            <span class="text-emerald-400 font-mono">● LIVE (2 min ago)</span>
                        </div>
                        <div class="flex justify-between items-center text-xs p-2 bg-slate-900/80 rounded border border-slate-800">
                            <span>Dibrugarh Marg ERP Connector (#STK-04)</span>
                            <span class="text-emerald-400 font-mono">● LIVE (14 min ago)</span>
                        </div>
                        <div class="flex justify-between items-center text-xs p-2 bg-slate-900/80 rounded border border-slate-800">
                            <span>Silchar Tally ERP Webhook (#STK-11)</span>
                            <span class="text-emerald-400 font-mono">● LIVE (28 min ago)</span>
                        </div>
                    </div>
                    <div class="text-[11px] text-slate-400 bg-slate-900 p-2.5 rounded font-mono border border-slate-800">
                        GxP Hash: <code>e8b4...90fc</code> · CDSCO Audit Trail: 100% Verified · Zero PII Collected
                    </div>
                </div>
            </div>

            <div class="pt-3 border-t border-slate-800 flex justify-end">
                <button onclick="closeAdminPanelModal()" class="px-4 py-2 rounded-lg bg-slate-700 hover:bg-slate-600 text-white font-semibold text-xs transition">
                    Close Console
                </button>
            </div>
        </div>
    </div>
"""

# Append modals before </body>
html = html.replace("</body>", modals_html + "\n</body>")

# Add JS functions to script
js_code_addition = """
        // Tutorial Modal Handlers
        function openTutorialModal() {
            document.getElementById('tutorialModal').classList.remove('hidden');
        }
        function closeTutorialModal() {
            document.getElementById('tutorialModal').classList.add('hidden');
        }

        // Admin Auth Handlers
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
                document.getElementById('adminLoginHeaderBtn').className = 'px-3.5 py-1.5 rounded-lg bg-emerald-600/30 hover:bg-emerald-600/50 text-emerald-200 border border-emerald-500/50 text-xs font-semibold flex items-center space-x-1.5 transition';
                document.getElementById('adminPanelModal').classList.remove('hidden');
            } else {
                document.getElementById('loginErrorMsg').classList.remove('hidden');
            }
        }

        function handleAdminLogout() {
            isAdminLoggedIn = false;
            closeAdminPanelModal();
            document.getElementById('adminHeaderLabel').innerText = 'Admin Panel (Login)';
            document.getElementById('adminLoginHeaderBtn').className = 'px-3.5 py-1.5 rounded-lg bg-purple-600/30 hover:bg-purple-600/50 text-purple-200 border border-purple-500/50 text-xs font-semibold flex items-center space-x-1.5 transition';
            alert('Admin logged out successfully.');
        }

        function toggleRouteStatus(route) {
            if (route === 'nh6') {
                const badge = document.getElementById('nh6StatusBadge');
                if (badge.innerText.includes('Flood')) {
                    badge.innerText = 'Normal';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-bold';
                } else {
                    badge.innerText = 'Flood Active';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-rose-950 text-rose-300 border border-rose-800 font-bold';
                }
            } else if (route === 'nh29') {
                const badge = document.getElementById('nh29StatusBadge');
                if (badge.innerText.includes('Caution')) {
                    badge.innerText = 'Normal';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 font-bold';
                } else {
                    badge.innerText = 'Caution';
                    badge.className = 'text-[10px] px-2 py-0.5 rounded bg-amber-950 text-amber-300 border border-amber-800 font-bold';
                }
            }
        }
"""

html = html.replace("// Initialize Lucide Icons", js_code_addition + "\n        // Initialize Lucide Icons")

with open("app/index.html", "w") as f:
    f.write(html)

print("app/index.html updated successfully with Tutorial and Admin features.")
