orbits(mercury, sun).  {facts}
orbits(venus,   sun).
orbits(earth,   sun).
orbits(mars,    sun).
orbits(jupiter, sun).
orbits(saturn,  sun).
orbits(uranus,  sun).
orbits(neptune, sun).

orbits(moon, earth).

orbits(deimos, mars).
orbits(phobos, mars).

orbits(ganymede, jupiter).
orbits(callisto, jupiter).
orbits(io,       jupiter).
orbits(europa,   jupiter).

orbits(titan,     saturn).
orbits(enceladus, saturn).

orbits(titania, uranus).
orbits(oberon,  uranus).
orbits(umbriel, uranus).
orbits(ariel,   uranus).
orbits(miranda, uranus).

orbits(triton, neptune).

planet(P)    <= orbits(P, sun).     {rules}
satellite(S) <= orbits(S, P) and planet(P).

? satellite(S).   {query}

orbits(mercury, sun).  {facts}
orbits(venus,   sun).
orbits(earth,   sun).
orbits(mars,    sun).
orbits(jupiter, sun).
orbits(saturn,  sun).
orbits(uranus,  sun).
orbits(neptune, sun).

orbits(moon, earth).

orbits(deimos, mars).
orbits(phobos, mars).
orbits(ganymede, jupiter).
orbits(callisto, jupiter).
orbits(io,       jupiter).
orbits(europa,   jupiter).

orbits(titan,     saturn).
orbits(enceladus, saturn).

orbits(titania, uranus).
orbits(oberon,  uranus).
orbits(umbriel, uranus).
orbits(ariel,   uranus).
orbits(miranda, uranus).

orbits(triton, neptune).

planet(P)    <= orbits(P, sun).     {rules}
satellite(S) <= orbits(S, P) and planet(P).

? satellite(S).   {query}


-- Parsing --
-- Running --
satellite(moon) yes
satellite(deimos) yes
satellite(phobos) yes
satellite(ganymede) yes
satellite(callisto) yes
satellite(io) yes
satellite(europa) yes
satellite(titan) yes
satellite(enceladus) yes
satellite(titania) yes
satellite(oberon) yes
satellite(umbriel) yes
satellite(ariel) yes
satellite(miranda) yes
satellite(triton) yes
