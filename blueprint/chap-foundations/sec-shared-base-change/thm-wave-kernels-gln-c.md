+++
kind  = "theorem"
title = "Wave kernels on the complex general linear group"
lean  = ["PositivityTheory.RgBcC.wave_existence_speed_multiplicity"]
order = 12
+++
Let $\tau$ be a finite-dimensional representation of $\U(n)$ and consider the
wave equation for $\tau$-valued functions on $\GL_n(\C)$. Then:

* the wave equation has a solution for all smooth compactly supported initial
  data of type $\tau$;
* it has finite propagation speed: there is $c$ such that a solution vanishes
  at $x$ at time $t$ if its initial data vanish on the ball of radius $c(1 + |t|)$
  around $x$;
* for every bump function $g$ of support $T$ there is a kernel supported in the
  ball of radius $c(1 + T)$ that acts on eigenfunctions of type $\tau$ by a
  multiplier determined by $g$ and the infinitesimal character;
* such kernels form an algebra: convolution multiplies the multipliers and is
  commutative, and the adjoint kernel has the conjugate multiplier.

This is the method of finite propagation speed (Chernoff; Cheeger, Gromov and
Taylor) for building test functions with given spherical transform.
