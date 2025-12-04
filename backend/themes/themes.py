THEMES = {
    "default": {
        "label": "Default",
        "description": "Clean, neutral light theme suitable for most business apps.",
        "intensity": "medium",

        # Tailwind tokens
        "bg_page": "bg-gray-50",
        "bg_surface": "bg-white",
        "bg_surface_elevated": "bg-white/90",
        "text_primary": "text-gray-900",
        "text_secondary": "text-gray-600",
        "text_muted": "text-gray-500",
        "accent": "text-blue-600",
        "accent_bg": "bg-blue-600",
        "accent_bg_hover": "hover:bg-blue-700",
        "border_subtle": "border-gray-200",

        # Fancy effects (guidelines)
        "effects": [
            "Use a very subtle radial gradient in the page background combining slate and blue tones.",
            "Cards should have soft shadows and slightly rounded corners (rounded-2xl shadow-lg).",
            "Buttons should slightly scale up on hover and use transition and shadow-md."
        ]
    },

    "dark": {
        "label": "Dark",
        "description": "Modern dark UI with neon-like accents and soft glows.",
        "intensity": "strong",

        "bg_page": "bg-gray-950",
        "bg_surface": "bg-gray-900",
        "bg_surface_elevated": "bg-gray-900/90",
        "text_primary": "text-gray-100",
        "text_secondary": "text-gray-400",
        "text_muted": "text-gray-500",
        "accent": "text-indigo-400",
        "accent_bg": "bg-indigo-500",
        "accent_bg_hover": "hover:bg-indigo-400",
        "border_subtle": "border-gray-800",

        "effects": [
            "Use a large multi-stop gradient background with deep blues and purples; think Linear.app style hero.",
            "Add glowing accent rings behind key CTAs using before/after pseudo-elements if needed.",
            "Cards should use subtle inner borders and outer shadows to float above the dark background.",
            "Use backdrop-blur and semi-transparent surfaces for a light glassmorphism feeling."
        ]
    },

    "glacier": {
        "label": "Glacier",
        "description": "Cool blue gradient backgrounds with icy highlights.",
        "intensity": "strong",

        "bg_page": "bg-sky-950",
        "bg_surface": "bg-slate-900/80",
        "bg_surface_elevated": "bg-slate-900/90",
        "text_primary": "text-slate-50",
        "text_secondary": "text-slate-300",
        "text_muted": "text-slate-400",
        "accent": "text-cyan-300",
        "accent_bg": "bg-cyan-400",
        "accent_bg_hover": "hover:bg-cyan-300",
        "border_subtle": "border-slate-700",

        "effects": [
            "Use a diagonal gradient hero from deep navy to cyan.",
            "Place a couple of blurred circular highlights using Tailwind utilities like bg-cyan-400/30 rounded-full blur-3xl.",
            "Cards should look icy: high contrast, light borders, and subtle glow on hover."
        ]
    },

    "lavender": {
        "label": "Lavender",
        "description": "Soft purple gradient theme suitable for personal or creative sites.",
        "intensity": "medium",

        "bg_page": "bg-gradient-to-br from-purple-900 via-slate-950 to-indigo-900",
        "bg_surface": "bg-slate-900/80",
        "bg_surface_elevated": "bg-slate-900/90",
        "text_primary": "text-slate-50",
        "text_secondary": "text-slate-300",
        "text_muted": "text-slate-400",
        "accent": "text-violet-300",
        "accent_bg": "bg-violet-500",
        "accent_bg_hover": "hover:bg-violet-400",
        "border_subtle": "border-violet-700",

        "effects": [
            "Use layered gradients with purple, indigo, and magenta.",
            "Use subtle glowing borders around primary buttons.",
            "Add small, slowly floating blurred blobs in the background for motion."
        ]
    },

    "obsidian": {
        "label": "Obsidian",
        "description": "Brutalist-inspired dark theme with strong contrast and minimal colors.",
        "intensity": "strong",

        "bg_page": "bg-black",
        "bg_surface": "bg-neutral-950",
        "bg_surface_elevated": "bg-neutral-900",
        "text_primary": "text-neutral-50",
        "text_secondary": "text-neutral-300",
        "text_muted": "text-neutral-500",
        "accent": "text-emerald-400",
        "accent_bg": "bg-emerald-500",
        "accent_bg_hover": "hover:bg-emerald-400",
        "border_subtle": "border-neutral-800",

        "effects": [
            "Use hard edges (rounded-none or rounded-md) and bold typography.",
            "Cards should have sharp drop shadows and clear separation lines.",
            "Avoid soft gradients; prefer solid backgrounds with a few neon accent lines or borders."
        ]
    }
}
