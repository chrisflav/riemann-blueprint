+++
id    = "thm-grh-from-sha-bound"
kind  = "theorem"
title = "GRH from the Tate–Shafarevich bound"
lean  = ["UpperTheory.LiteratureTheorems.every_character_of_literature_of_vWin",
         "UpperTheory.LiteratureTheorems.OpenLiteratureStatements",
         "UpperTheory.LiteratureTheorems.published_results_eigen",
         "UpperTheory.LiteratureTheorems.published_results_first"]
uses  = ["def-sha-bound", "def-galois-reps-polarized", "def-local-parameters",
         "def-nonvanishing-half-plane"]
order = 4
+++
Suppose that polarized pairs have Galois representations
([def-galois-reps-polarized]) for a system of local parameters
([def-local-parameters]), and that the Tate–Shafarevich bound
([def-sha-bound]) holds with exponent $401$. Then Dirichlet $L$-functions do
not vanish right of the critical line.
