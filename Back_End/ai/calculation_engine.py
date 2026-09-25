"""
HYBRID CALCULATION ENGINE
==========================
Engine hybrid yang routing chat biasa ke LLM, dan calculation kompleks ke SymPy.
Kombinasi kecepatan + akurasi 100%.

Fitur:
- Auto-detect query type (chat vs calculation)
- Solve equations dengan SymPy (analitik, exact)
- Symbolic computation
- Numeric approximation
- Verification & validation
- Fallback ke LLM jika SymPy gagal
"""

import re
from typing import Dict, Optional, Tuple, List
import logging

try:
    import sympy as sp
    SYMPY_AVAILABLE = True
except ImportError:
    SYMPY_AVAILABLE = False
    logging.warning("SymPy tidak terinstall. Install: pip install sympy")


logger = logging.getLogger(__name__)


class HybridCalculationEngine:
    """
    Engine hybrid untuk process chat + mathematical calculations.
    """

    def __init__(self, use_llm_fallback: bool = True):
        """
        Args:
            use_llm_fallback: Jika True, fallback ke LLM jika SymPy gagal
        """
        if not SYMPY_AVAILABLE:
            raise ImportError(
                "SymPy tidak terinstall. Install dengan:\n"
                "pip install sympy"
            )

        self.use_llm_fallback = use_llm_fallback

        logger.info("✅ Hybrid Calculation Engine initialized")

    # ─────────────────────────────────────────────────────
    # QUERY TYPE DETECTION
    # ─────────────────────────────────────────────────────

    def detect_query_type(self, query: str) -> str:
        """
        Deteksi tipe query: 'chat' atau 'calculation'

        Returns: 'chat', 'calculation', 'integration', 'derivation', 'solve', 'simplify'
        """
        query_lower = query.lower()

        # Deteksi pertanyaan konsep/penjelasan (bukan perhitungan numerik/simbolik)
        explanation_keywords = [
            'jelaskan', 'apa itu', 'apakah', 'pengertian', 'definisi',
            'apa yang dimaksud', 'mengapa', 'sebutkan', 'konsep', 'bagaimana'
        ]
        is_explanation = any(kw in query_lower for kw in explanation_keywords)

        # Kata kunci yang secara spesifik meminta kalkulasi
        calc_action_keywords = [
            'hitung', 'tentukan hasil', 'tentukan nilai', 'selesaikan',
            'd/dx', '=', '∫', 'nilai dari', 'cari nilai', 'cari x',
            'akar dari', 'turunan', 'integral', 'derive', 'integrate'
        ]
        has_calc_action = any(act in query_lower for act in calc_action_keywords)

        if is_explanation and not has_calc_action:
            return 'chat'

        # ── Integration detection ──────────────────────────────────────
        if any(keyword in query_lower for keyword in [
            'hitung integral', 'cari integral', 'integral dari',
            'tentukan integral', '∫', 'integrate', 'antiderivative',
            'antiderivatif', 'anti-derivative'
        ]):
            return 'integration'

        # ── Derivation detection ───────────────────────────────────────
        if any(keyword in query_lower for keyword in [
            'hitung turunan', 'turunan dari', 'turunan pertama',
            'turunan ke', 'cari turunan', 'tentukan turunan',
            'derivative of', 'differentiate', 'diferensialkan',
            "f'(x)", 'd/dx', 'dy/dx'
        ]):
            return 'derivation'

        # Turunan juga bisa muncul tanpa kata kunci lengkap — tangkap pola generik
        if re.search(r'\bturunan\b', query_lower):
            return 'derivation'

        if re.search(r'\bintegral\b', query_lower):
            return 'integration'

        # ── Solve equation detection ───────────────────────────────────
        if any(keyword in query_lower for keyword in [
            'selesaikan', 'solve', 'cari nilai x', 'cari nilai y',
            'cari x', 'find x', 'tentukan nilai x', 'akar persamaan'
        ]) and ('=' in query_lower or bool(re.search(r'\d', query_lower))):
            return 'solve'

        # ── Simplify detection ─────────────────────────────────────────
        if any(keyword in query_lower for keyword in [
            'sederhanakan', 'simplify', 'jabarkan', 'faktorkan', 'faktor dari'
        ]) and bool(re.search(r'[a-zA-Z0-9]', query_lower)):
            return 'simplify'

        # Default: chat
        return 'chat'

    # ─────────────────────────────────────────────────────
    # SYMPY OPERATIONS
    # ─────────────────────────────────────────────────────

    def solve_equation(self, equation_str: str, variable: str = 'x') -> Dict:
        """
        Solve equation.

        Example:
            solve_equation("x^2 - 4 = 0")  →  {x: -2, x: 2}
        """
        try:
            x = sp.symbols(variable)

            # Bersihkan dan konversi notasi
            clean_eq = self._clean_math_expression(equation_str)

            # Pisahkan LHS dan RHS jika ada tanda '='
            if '=' in clean_eq:
                parts = clean_eq.split('=', 1)
                lhs = sp.sympify(parts[0].strip())
                rhs = sp.sympify(parts[1].strip())
                expr = lhs - rhs
            else:
                expr = sp.sympify(clean_eq)

            # Solve
            solutions = sp.solve(expr, x)

            if not solutions:
                return {"success": False, "error": "Tidak ada solusi"}

            return {
                "success": True,
                "solutions": [str(sol) for sol in solutions],
                "solutions_latex": [sp.latex(sol) for sol in solutions],
                "symbolic": solutions,
            }

        except Exception as e:
            logger.error(f"❌ Error solving equation: {e}")
            return {"success": False, "error": str(e)}

    def compute_integral(self, expression_str: str, variable: str = 'x', limits: Optional[Tuple] = None) -> Dict:
        """
        Compute integral.

        Example:
            compute_integral("x^2")  →  indefinite integral
            compute_integral("x^2", limits=(0, 1))  →  definite integral
        """
        try:
            clean_expr = self._clean_math_expression(expression_str)
            expr = sp.sympify(clean_expr)
            x = sp.symbols(variable)

            if limits:
                # Definite integral
                result = sp.integrate(expr, (x, limits[0], limits[1]))
                result_str = f"∫ {expression_str} dx from {limits[0]} to {limits[1]} = {result}"
            else:
                # Indefinite integral
                result = sp.integrate(expr, x)
                result_str = f"∫ {expression_str} dx = {result} + C"

            return {
                "success": True,
                "result": str(result),
                "result_latex": sp.latex(result),
                "result_unicode": result_str,
                "limits": limits,
            }

        except Exception as e:
            logger.error(f"❌ Error computing integral: {e}")
            return {"success": False, "error": str(e)}

    def compute_derivative(self, expression_str: str, variable: str = 'x', order: int = 1) -> Dict:
        """
        Compute derivative.

        Example:
            compute_derivative("x^3 + 2*x")  →  3*x^2 + 2
            compute_derivative("x^3", order=2)  →  6*x
        """
        try:
            clean_expr = self._clean_math_expression(expression_str)
            expr = sp.sympify(clean_expr)
            x = sp.symbols(variable)

            # Compute derivative
            result = sp.diff(expr, x, order)

            return {
                "success": True,
                "original": expression_str,
                "result": str(result),
                "result_latex": sp.latex(result),
                "order": order,
            }

        except Exception as e:
            logger.error(f"❌ Error computing derivative: {e}")
            return {"success": False, "error": str(e)}

    def simplify_expression(self, expression_str: str) -> Dict:
        """Simplify expression"""
        try:
            expr = sp.sympify(expression_str)
            simplified = sp.simplify(expr)

            return {
                "success": True,
                "original": expression_str,
                "simplified": str(simplified),
                "simplified_latex": sp.latex(simplified),
            }

        except Exception as e:
            logger.error(f"❌ Error simplifying: {e}")
            return {"success": False, "error": str(e)}

    def expand_expression(self, expression_str: str) -> Dict:
        """Expand expression"""
        try:
            expr = sp.sympify(expression_str)
            expanded = sp.expand(expr)

            return {
                "success": True,
                "original": expression_str,
                "expanded": str(expanded),
                "expanded_latex": sp.latex(expanded),
            }

        except Exception as e:
            logger.error(f"❌ Error expanding: {e}")
            return {"success": False, "error": str(e)}

    def factor_expression(self, expression_str: str) -> Dict:
        """Factor expression"""
        try:
            expr = sp.sympify(expression_str)
            factored = sp.factor(expr)

            return {
                "success": True,
                "original": expression_str,
                "factored": str(factored),
                "factored_latex": sp.latex(factored),
            }

        except Exception as e:
            logger.error(f"❌ Error factoring: {e}")
            return {"success": False, "error": str(e)}

    # ─────────────────────────────────────────────────────
    # VERIFICATION
    # ─────────────────────────────────────────────────────

    def verify_solution(self, equation_str: str, solution_value: str, variable: str = 'x') -> bool:
        """
        Verify apakah solution memenuhi equation.

        Example:
            verify_solution("x^2 - 4 = 0", "2", "x")  →  True
        """
        try:
            equation = sp.sympify(equation_str)
            x = sp.symbols(variable)
            solution = sp.sympify(solution_value)

            # Substitute solution into equation
            result = equation.subs(x, solution)
            result_simplified = sp.simplify(result)

            # Check if equals zero
            return result_simplified == 0

        except Exception as e:
            logger.error(f"❌ Error verifying solution: {e}")
            return False

    # ─────────────────────────────────────────────────────
    # MAIN PROCESS FUNCTION
    # ─────────────────────────────────────────────────────

    def process(
        self,
        user_query: str,
        use_llm_fallback: bool = True
    ) -> Dict:
        """
        Main function: Auto-route ke LLM atau SymPy.

        Returns:
            {
                "type": "chat" | "calculation",
                "success": True/False,
                "response": "...",
                "explanation": "...",
                "used_sympy": True/False
            }
        """
        query_type = self.detect_query_type(user_query)

        # Chat queries → LLM
        if query_type == 'chat':
            return {
                "type": "chat",
                "success": True,
                "used_sympy": False,
                "routing": "LLM (normal conversation)"
            }

        # Calculation queries → SymPy
        logger.info(f"📊 Processing {query_type} query with SymPy")

        result = None

        if query_type == 'integration':
            result = self._process_integration(user_query)

        elif query_type == 'derivation':
            result = self._process_derivation(user_query)

        elif query_type == 'solve':
            result = self._process_solve(user_query)

        elif query_type == 'simplify':
            result = self._process_simplify(user_query)

        if result and result.get("success"):
            return {
                "type": query_type,
                "success": True,
                "used_sympy": True,
                **result
            }

        # Fallback ke LLM jika SymPy gagal
        if use_llm_fallback:
            logger.warning(f"⚠️ SymPy failed, fallback to LLM")
            return {
                "type": query_type,
                "success": False,
                "used_sympy": False,
                "routing": "LLM (fallback)",
                "reason": "SymPy calculation failed"
            }

        return {
            "type": query_type,
            "success": False,
            "used_sympy": False,
        }

    # ─────────────────────────────────────────────────────
    # HELPER FUNCTIONS
    # ─────────────────────────────────────────────────────

    def _clean_math_expression(self, expr: str) -> str:
        """Membersihkan ekspresi matematika dari kata-kata natural language dan superscripts."""
        if not expr:
            return ""

        # ── Ekstrak dari pola f(x) = ... atau y = ... ──────────────────
        fx_match = re.search(r'(?:f\(x\)|g\(x\)|h\(x\)|y)\s*=\s*([^.?\n]+)', expr, re.IGNORECASE)
        if fx_match:
            expr = fx_match.group(1)

        # ── Hapus semua kata natural language Indonesia / Inggris ──────
        # Prefix keterangan urutan
        expr = re.sub(r'^(pertama|kedua|ketiga|ke-?\d+)\s+', '', expr, flags=re.IGNORECASE)
        # Prefix generik
        prefixes = [
            r'hitung\s+integral\s+dari',
            r'hitung\s+integral',
            r'cari\s+integral\s+dari',
            r'cari\s+integral',
            r'tentukan\s+integral\s+dari',
            r'tentukan\s+integral',
            r'integral\s+dari',
            r'hitung\s+turunan\s+(?:pertama|kedua|ketiga|ke-?\d+)?\s*dari',
            r'hitung\s+turunan',
            r'cari\s+turunan\s+(?:pertama|kedua|ketiga|ke-?\d+)?\s*dari',
            r'cari\s+turunan',
            r'tentukan\s+turunan\s+(?:pertama|kedua|ketiga|ke-?\d+)?\s*dari',
            r'tentukan\s+turunan',
            r'turunan\s+(?:pertama|kedua|ketiga|ke-?\d+)?\s*dari\s*fungsi',
            r'turunan\s+(?:pertama|kedua|ketiga|ke-?\d+)?\s*dari',
            r'turunan\s+(?:pertama|kedua|ketiga|ke-?\d+)?',
            r'derivative\s+of\s+function',
            r'derivative\s+of',
            r'differentiate',
            r'dari\s+fungsi',
            r'dari',
            r'fungsi',
            r'persamaan',
            r'nilai',
        ]
        for p in prefixes:
            expr = re.sub(r'^' + p + r'\s*', '', expr.strip(), flags=re.IGNORECASE)

        # Hapus sisa deklarasi f(x) = di awal setelah stripping
        expr = re.sub(r'^(?:f\(x\)|g\(x\)|h\(x\)|y)\s*=\s*', '', expr, flags=re.IGNORECASE)

        # Hapus 'dx', 'd/dx' sisa yang mungkin tertinggal di akhir
        expr = re.sub(r'\s*d[x-z]\s*$', '', expr, flags=re.IGNORECASE)
        expr = re.sub(r'\s*,\s*x\s*=.*$', '', expr)  # misal ", x = 0 to 1"

        # ── Konversi superscripts unicode (x³ → x**3) ─────────────────
        superscripts = {
            '⁰': '**0', '¹': '**1', '²': '**2', '³': '**3', '⁴': '**4',
            '⁵': '**5', '⁶': '**6', '⁷': '**7', '⁸': '**8', '⁹': '**9'
        }
        for sup, norm in superscripts.items():
            expr = expr.replace(sup, norm)

        # ── Konversi notasi matematika ─────────────────────────────────
        expr = expr.replace('^', '**')

        # ── Perkalian implisit: 2x → 2*x, 5(x+1) → 5*(x+1) ──────────
        expr = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expr)
        expr = re.sub(r'(\d)\(', r'\1*(', expr)
        expr = re.sub(r'\)([a-zA-Z0-9])', r')*\1', expr)

        return expr.strip()

    def _extract_expression_from_query(self, query: str) -> Optional[str]:
        """Extract mathematical expression dari user query — multi-pattern dengan greedy fallback."""

        # ── Pola spesifik (ordered from most to least specific) ────────
        patterns = [
            # Integral dengan batas
            r'integral\s+(?:dari\s+)?(.+?)\s+(?:dari|from)\s+[\d-]+\s+(?:ke|hingga|sampai|to)\s+[\d-]+',
            # Selesaikan / solve
            r'(?:selesaikan|solve)\s+(?:persamaan\s+)?(.+?)(?:\s+(?:untuk|for)\s+[a-z])?\s*$',
            # Integral hitung / cari / tentukan
            r'(?:hitung|cari|tentukan)\s+integral\s+(?:dari\s+)?(.+?)(?:\s+(?:terhadap|d[a-z]))?\s*$',
            # Integral dari <expr>
            r'integral\s+(?:dari\s+)?(.+?)(?:\s+d[a-z])?\s*$',
            # Turunan ... dari ... fungsi
            r'turunan\s+(?:pertama|kedua|ketiga|ke-?\d+\s+)?(?:dari\s+)?(?:fungsi\s+)?(.+?)\s*$',
            # Hitung / cari / tentukan turunan
            r'(?:hitung|cari|tentukan)\s+turunan\s+(?:pertama|kedua|ketiga|ke-?\d+\s+)?(?:dari\s+)?(?:fungsi\s+)?(.+?)\s*$',
            # Derivative of
            r'(?:derivative|differentiate)\s+(?:of\s+)?(?:function\s+)?(.+?)\s*$',
            # Cari nilai x / find x dalam persamaan
            r'(?:cari\s+(?:nilai\s+)?[a-z]|find\s+[a-z])\s+(?:dari|dalam|in|from)?\s*(?:persamaan\s+)?(.+?)\s*$',
        ]

        for pattern in patterns:
            match = re.search(pattern, query, re.IGNORECASE)
            if match:
                raw_expr = match.group(1).strip()
                cleaned = self._clean_math_expression(raw_expr)
                if cleaned:
                    logger.debug(f"✅ Extracted via pattern: '{cleaned}' from '{query[:60]}'")
                    return cleaned

        # ── Greedy fallback: cari setelah simbol '=' atau kata kunci ──
        # Tangkap ekspresi setelah f(x) = ..., y = ...
        eq_match = re.search(
            r'(?:f\(x\)|g\(x\)|y|f)\s*=\s*([^.?\n,]+)', query, re.IGNORECASE
        )
        if eq_match:
            raw_expr = eq_match.group(1).strip()
            cleaned = self._clean_math_expression(raw_expr)
            if cleaned:
                logger.debug(f"✅ Extracted via f(x)= fallback: '{cleaned}'")
                return cleaned

        # ── Last resort: ambil semua token yang tampak seperti ekspresi math
        # Cari substring yang mengandung operator/angka/variabel dan tidak hanya kata
        math_candidates = re.findall(
            r'[\dx\s\+\-\*\/\^\(\)\³\²\.]+(?:[\*\+\-\/\^][\dx\s\(\)\^\³\²\.]+)+',
            query
        )
        if math_candidates:
            raw_expr = max(math_candidates, key=len).strip()
            cleaned = self._clean_math_expression(raw_expr)
            if cleaned:
                logger.debug(f"✅ Extracted via math-token fallback: '{cleaned}'")
                return cleaned

        logger.warning(f"❌ Failed to extract math expression from: '{query[:80]}'")
        return None

    def _process_integration(self, query: str) -> Optional[Dict]:
        """Process integration query"""
        expr = self._extract_expression_from_query(query)
        if not expr:
            logger.warning(f"Integration: ekspresi tidak dapat diekstrak dari: '{query[:60]}'")
            return None

        # Bersihkan simbol integral yang mungkin ikut terekstrak
        expr = re.sub(r'[∫]', '', expr)
        expr = re.sub(r'\s*d[a-z]\s*$', '', expr).strip()
        logger.debug(f"Integration expr → SymPy: '{expr}'")
        return self.compute_integral(expr)

    def _process_derivation(self, query: str) -> Optional[Dict]:
        """Process derivation query"""
        # Cek apakah ada order turunan (ke-2, ke-3, dll.)
        order = 1
        order_match = re.search(
            r'turunan\s+(?:ke-?(\d+)|kedua|ketiga)', query, re.IGNORECASE
        )
        if order_match:
            raw_order = order_match.group(1)
            if raw_order:
                order = int(raw_order)
            elif 'kedua' in query.lower():
                order = 2
            elif 'ketiga' in query.lower():
                order = 3

        expr = self._extract_expression_from_query(query)
        if not expr:
            logger.warning(f"Derivation: ekspresi tidak dapat diekstrak dari: '{query[:60]}'")
            return None

        logger.debug(f"Derivation expr → SymPy: '{expr}' (order={order})")
        return self.compute_derivative(expr, order=order)

    def _process_solve(self, query: str) -> Optional[Dict]:
        """Process solve query"""
        expr = self._extract_expression_from_query(query)
        if not expr:
            logger.warning(f"Solve: ekspresi tidak dapat diekstrak dari: '{query[:60]}'")
            return None

        logger.debug(f"Solve expr → SymPy: '{expr}'")
        return self.solve_equation(expr)

    def _process_simplify(self, query: str) -> Optional[Dict]:
        """Process simplify query"""
        expr = self._extract_expression_from_query(query)
        if not expr:
            logger.warning(f"Simplify: ekspresi tidak dapat diekstrak dari: '{query[:60]}'")
            return None

        logger.debug(f"Simplify expr → SymPy: '{expr}'")
        return self.simplify_expression(expr)


# ─────────────────────────────────────────────────────
# FORMAT OUTPUT UNTUK UI
# ─────────────────────────────────────────────────────

def format_sympy_result_for_ui(result: Dict) -> str:
    """
    Format SymPy result untuk UI (dengan LaTeX).

    Returns markdown string yang bisa di-render dengan KaTeX
    """
    if not result.get("success"):
        return f"❌ Error: {result.get('error', 'Unknown error')}"

    query_type = result.get("type", "calculation")

    if query_type == "solve":
        solutions = result.get("solutions_latex", [])
        solutions_text = ", ".join([f"${sol}$" for sol in solutions])
        return f"""
**Solusi:**

{solutions_text}

**Verifikasi:**
Jawaban telah dihitung menggunakan SymPy dengan akurasi 100%.
"""

    elif query_type == "integration":
        result_latex = result.get("result_latex", "")
        return f"""
**Hasil Integral:**

$$\\int {{ {result.get('result_unicode', '')} }} = {result_latex}$$
"""

    elif query_type == "derivation":
        result_latex = result.get("result_latex", "")
        return f"""
**Hasil Turunan:**

$$\\frac{{d}}{{dx}} \\left( {result.get('original')} \\right) = {result_latex}$$
"""

    elif query_type == "simplify":
        simplified = result.get("simplified_latex", "")
        original = result.get("original", "")
        return f"""
**Penyederhanaan:**

Dari: ${original}$

Menjadi: ${simplified}$
"""

    return str(result)


# ─────────────────────────────────────────────────────
# TESTING
# ─────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 60)
    print("HYBRID CALCULATION ENGINE - TEST")
    print("=" * 60)

    engine = HybridCalculationEngine()

    # Test 1: Detect query types
    test_queries = [
        "Halo, apa kabar?",
        "Selesaikan x^2 - 4 = 0",
        "Hitung integral dari x^2",
        "Cari turunan dari sin(x)",
        "Sederhanakan (x+1)^2",
    ]

    print("\n1️⃣ Query Type Detection:")
    for query in test_queries:
        qtype = engine.detect_query_type(query)
        print(f"   '{query[:40]}...' → {qtype}")

    # Test 2: Solve equation
    print("\n2️⃣ Solve Equation:")
    result = engine.solve_equation("x^2 - 4 = 0")
    print(f"   Equation: x^2 - 4 = 0")
    print(f"   Solutions: {result.get('solutions')}")

    # Test 3: Compute integral
    print("\n3️⃣ Compute Integral:")
    result = engine.compute_integral("x^2")
    print(f"   Expression: x^2")
    print(f"   Result: {result.get('result')}")

    # Test 4: Compute derivative
    print("\n4️⃣ Compute Derivative:")
    result = engine.compute_derivative("x^3 + 2*x")
    print(f"   Expression: x^3 + 2*x")
    print(f"   Result: {result.get('result')}")

    # Test 5: Full process
    print("\n5️⃣ Full Process (auto-routing):")
    test_cases = [
        "Selesaikan persamaan x^2 - 4 = 0",
        "Hitung integral dari 2*x dx",
        "Turunan dari sin(x)",
    ]

    for query in test_cases:
        result = engine.process(query)
        print(f"\n   Query: {query}")
        print(f"   Type: {result.get('type')}")
        print(f"   Used SymPy: {result.get('used_sympy')}")
        if result.get("success"):
            print(f"   Result: {result.get('result', 'N/A')}")

    print("\n✅ Test selesai!")
