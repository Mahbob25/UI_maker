THEMES = {
    "default": {
        "name": "Default",
        "description": "Clean and professional light mode with subtle shadows and blue accents",
        "background": "bg-gray-50",
        "colors": { 
            "surface": "bg-white",
            "card": "bg-white",
            "input": "bg-white border border-gray-300 text-gray-900 placeholder-gray-500",
            "button": "bg-blue-600 text-white",
            "button_hover": "hover:bg-blue-700",
            "heading": "text-gray-900",
            "text": "text-gray-700",
            "accent": "text-blue-600",
        },
        "effects": { 
            "card_shadow": "shadow-lg",
            "button_shadow": "shadow-md",
            "hover_glow": "transition duration-300",
            "transition": "transition duration-200 ease-out",
        },
        "radius": { 
            "card": "rounded-xl",
            "button": "rounded-lg",
            "input": "rounded-md",
        }
    },

    "nebula_dark": {
        "name": "Nebula Dark",
        "description": "Deep cosmic purple gradient with glowing glassmorphic cards — perfect for night owls",
        "background": "bg-gradient-to-br from-[#0f0c29] via-[#302b63] to-[#24243e]",
        "colors": { 
            "surface": "bg-[#1b1a2e]/80 backdrop-blur-xl",
            "card": "bg-[#1f1d36]/90 backdrop-blur-xl",
            "input": "bg-[#2a2843] border border-[#3a375a] text-gray-200 placeholder-gray-500",
            "button": "bg-[#6c63ff] text-white",
            "button_hover": "hover:bg-[#5a52dd]",
            "heading": "text-[#b9b4ff]",
            "text": "text-gray-300",
            "accent": "text-[#6c63ff]",
         },
        "effects": { 
            "card_shadow": "shadow-[0_0_20px_rgba(108,99,255,0.25)]",
            "button_shadow": "shadow-[0_0_12px_rgba(108,99,255,0.35)]",
            "hover_glow": "hover:shadow-[0_0_18px_rgba(108,99,255,0.45)]",
            "transition": "transition-all duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-2xl",
            "button": "rounded-xl",
            "input": "rounded-lg",
         }
    },

    "sunrise": {
        "name": "Sunrise",
        "description": "Warm, uplifting gradient of orange, rose, and purple — like watching dawn from your desk",
        "background": "bg-gradient-to-br from-orange-100 via-rose-100 to-purple-100",
        "colors": { 
            "surface": "bg-white/80 backdrop-blur",
            "card": "bg-white/90 backdrop-blur-md",
            "input": "bg-white border border-gray-300 text-gray-800 placeholder-gray-400",
            "button": "bg-orange-500 text-white",
            "button_hover": "hover:bg-orange-600",
            "heading": "text-orange-600",
            "text": "text-gray-700",
            "accent": "text-orange-500",
         },
        "effects": { 
            "card_shadow": "shadow-xl shadow-orange-200",
            "button_shadow": "shadow-md shadow-orange-300",
            "hover_glow": "hover:shadow-lg hover:shadow-orange-300",
            "transition": "transition duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-2xl",
            "button": "rounded-lg",
            "input": "rounded-lg",
         }
    },

    "cyber_neon": {
        "name": "Cyber Neon",
        "description": "Intense synthwave cyberpunk vibe with electric cyan-purple glows and retro-futuristic energy",
        "background": "bg-gradient-to-br from-[#0a0028] via-[#1a0033] to-[#2d0055]",
        "colors": { 
            "surface": "bg-black/70 backdrop-blur-xl",
            "card": "bg-[#120030]/80 backdrop-blur-2xl border border-purple-500/30",
            "input": "bg-[#1a0a3e] border border-cyan-500/50 text-cyan-300 placeholder-cyan-700",
            "button": "bg-gradient-to-r from-cyan-500 to-purple-600 text-white",
            "button_hover": "hover:from-cyan-400 hover:to-purple-500",
            "heading": "text-cyan-300",
            "text": "text-purple-200",
            "accent": "text-cyan-400",
         },
        "effects": { 
            "card_shadow": "shadow-[0_0_30px_rgba(0,255,255,0.3)]",
            "button_shadow": "shadow-[0_0_20px_rgba(168,85,247,0.6)]",
            "hover_glow": "hover:shadow-[0_0_35px_rgba(0,255,255,0.5)] transition-all duration-400",
            "transition": "transition-all duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-2xl",
            "button": "rounded-xl",
            "input": "rounded-lg",
         }
    },

    "emerald_luxe": {
        "name": "Emerald Luxe",
        "description": "Sophisticated dark nature theme inspired by deep forests and luxury jewelry",
        "background": "bg-gradient-to-br from-emerald-950 via-teal-900 to-slate-900",
        "colors": { 
            "surface": "bg-emerald-950/80 backdrop-blur-xl",
            "card": "bg-emerald-900/70 backdrop-blur-xl border border-emerald-700/50",
            "input": "bg-emerald-800/60 border border-emerald-600 text-emerald-100 placeholder-emerald-400",
            "button": "bg-gradient-to-r from-emerald-600 to-teal-600 text-white",
            "button_hover": "hover:from-emerald-500 hover:to-teal-500",
            "heading": "text-emerald-300",
            "text": "text-emerald-200",
            "accent": "text-emerald-400",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-emerald-900/60",
            "button_shadow": "shadow-lg shadow-emerald-700/70",
            "hover_glow": "hover:shadow-emerald-500/40 hover:shadow-2xl",
            "transition": "transition-all duration-400 ease-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-2xl",
            "input": "rounded-xl",
         }
    },

    "rose_gold": {
        "name": "Rose Gold",
        "description": "Elegant, feminine, and luxurious — soft pinks with warm metallic undertones",
        "background": "bg-gradient-to-br from-rose-100 via-pink-100 to-amber-50",
        "colors": { 
            "surface": "bg-white/90 backdrop-blur-md",
            "card": "bg-white/95 backdrop-blur-lg border border-rose-200",
            "input": "bg-rose-50 border border-rose-300 text-rose-900 placeholder-rose-400",
            "button": "bg-gradient-to-r from-rose-500 to-pink-500 text-white",
            "button_hover": "hover:from-rose-600 hover:to-pink-600",
            "heading": "text-rose-800",
            "text": "text-rose-700",
            "accent": "text-rose-600",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-rose-200",
            "button_shadow": "shadow-xl shadow-rose-300",
            "hover_glow": "hover:shadow-2xl hover:shadow-rose-300/60",
            "transition": "transition-all duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-full",
            "input": "rounded-2xl",
         }
    },

    "arctic_frost": {
        "name": "Arctic Frost",
        "description": "Crisp, minimalist light theme with icy cyan-blue touches and airy glass effects",
        "background": "bg-gradient-to-br from-slate-50 via-blue-50 to-cyan-50",
        "colors": { 
            "surface": "bg-white/80 backdrop-blur-xl",
            "card": "bg-white/90 backdrop-blur-2xl border border-cyan-200/50",
            "input": "bg-white/70 border border-cyan-300 text-slate-800 placeholder-slate-400",
            "button": "bg-gradient-to-r from-cyan-500 to-blue-600 text-white",
            "button_hover": "hover:from-cyan-400 hover:to-blue-500",
            "heading": "text-slate-800",
            "text": "text-slate-600",
            "accent": "text-cyan-600",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-cyan-100",
            "button_shadow": "shadow-lg shadow-cyan-200",
            "hover_glow": "hover:shadow-xl hover:shadow-cyan-300/50",
            "transition": "transition-all duration-300 ease-in-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-2xl",
            "input": "rounded-xl",
         }
    },

    "midnight_amber": {
        "name": "Midnight Amber",
        "description": "Warm, cozy dark theme with rich amber and bronze tones — like a high-end whiskey lounge",
        "background": "bg-gradient-to-br from-amber-950 via-orange-950 to-stone-950",
        "colors": {
            "surface": "bg-black/80 backdrop-blur-xl",
            "card": "bg-amber-950/90 backdrop-blur-2xl border border-amber-800/40",
            "input": "bg-amber-900/50 border border-amber-700 text-amber-200 placeholder-amber-500",
            "button": "bg-gradient-to-r from-amber-600 to-orange-600 text-white",
            "button_hover": "hover:from-amber-500 hover:to-orange-500",
            "heading": "text-amber-300",
            "text": "text-amber-200",
            "accent": "text-amber-400",
            },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-amber-900/60",
            "button_shadow": "shadow-xl shadow-amber-800/80",
            "hover_glow": "hover:shadow-amber-600/50 hover:shadow-2xl",
            "transition": "transition-all duration-500 ease-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-2xl",
            "input": "rounded-xl",
         }
    },

    "oceanic_deep": {
        "name": "Oceanic Deep",
        "description": "Immersive underwater feel with deep navy blues and glowing cyan highlights",
        "background": "bg-gradient-to-br from-[#001d3d] via-[#003366] to-[#000080]",
        "colors": { 
            "surface": "bg-[#0a1d37]/80 backdrop-blur-xl",
            "card": "bg-[#0f2b52]/80 backdrop-blur-2xl border border-cyan-800/30",
            "input": "bg-[#0f2b52]/60 border border-cyan-600/50 text-cyan-100 placeholder-cyan-500",
            "button": "bg-gradient-to-r from-cyan-600 via-blue-600 to-indigo-600 text-white",
            "button_hover": "hover:from-cyan-500 hover:via-blue-500 hover:to-indigo-500",
            "heading": "text-cyan-200",
            "text": "text-blue-200",
            "accent": "text-cyan-400",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-cyan-900/50",
            "button_shadow": "shadow-lg shadow-cyan-700/70",
            "hover_glow": "hover:shadow-[0_0_30px_rgba(34,211,238,0.5)]",
            "accent": "text-[#6c63ff]",
         },
        "effects": { 
            "card_shadow": "shadow-[0_0_20px_rgba(108,99,255,0.25)]",
            "button_shadow": "shadow-[0_0_12px_rgba(108,99,255,0.35)]",
            "hover_glow": "hover:shadow-[0_0_18px_rgba(108,99,255,0.45)]",
            "transition": "transition-all duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-2xl",
            "button": "rounded-xl",
            "input": "rounded-lg",
         }
    },

    "sunrise": {
        "name": "Sunrise",
        "description": "Warm, uplifting gradient of orange, rose, and purple — like watching dawn from your desk",
        "background": "bg-gradient-to-br from-orange-100 via-rose-100 to-purple-100",
        "colors": { 
            "surface": "bg-white/80 backdrop-blur",
            "card": "bg-white/90 backdrop-blur-md",
            "input": "bg-white border border-gray-300 text-gray-800 placeholder-gray-400",
            "button": "bg-orange-500 text-white",
            "button_hover": "hover:bg-orange-600",
            "heading": "text-orange-600",
            "text": "text-gray-700",
            "accent": "text-orange-500",
         },
        "effects": { 
            "card_shadow": "shadow-xl shadow-orange-200",
            "button_shadow": "shadow-md shadow-orange-300",
            "hover_glow": "hover:shadow-lg hover:shadow-orange-300",
            "transition": "transition duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-2xl",
            "button": "rounded-lg",
            "input": "rounded-lg",
         }
    },

    "cyber_neon": {
        "name": "Cyber Neon",
        "description": "Intense synthwave cyberpunk vibe with electric cyan-purple glows and retro-futuristic energy",
        "background": "bg-gradient-to-br from-[#0a0028] via-[#1a0033] to-[#2d0055]",
        "colors": { 
            "surface": "bg-black/70 backdrop-blur-xl",
            "card": "bg-[#120030]/80 backdrop-blur-2xl border border-purple-500/30",
            "input": "bg-[#1a0a3e] border border-cyan-500/50 text-cyan-300 placeholder-cyan-700",
            "button": "bg-gradient-to-r from-cyan-500 to-purple-600 text-white",
            "button_hover": "hover:from-cyan-400 hover:to-purple-500",
            "heading": "text-cyan-300",
            "text": "text-purple-200",
            "accent": "text-cyan-400",
         },
        "effects": { 
            "card_shadow": "shadow-[0_0_30px_rgba(0,255,255,0.3)]",
            "button_shadow": "shadow-[0_0_20px_rgba(168,85,247,0.6)]",
            "hover_glow": "hover:shadow-[0_0_35px_rgba(0,255,255,0.5)] transition-all duration-400",
            "transition": "transition-all duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-2xl",
            "button": "rounded-xl",
            "input": "rounded-lg",
         }
    },

    "emerald_luxe": {
        "name": "Emerald Luxe",
        "description": "Sophisticated dark nature theme inspired by deep forests and luxury jewelry",
        "background": "bg-gradient-to-br from-emerald-950 via-teal-900 to-slate-900",
        "colors": { 
            "surface": "bg-emerald-950/80 backdrop-blur-xl",
            "card": "bg-emerald-900/70 backdrop-blur-xl border border-emerald-700/50",
            "input": "bg-emerald-800/60 border border-emerald-600 text-emerald-100 placeholder-emerald-400",
            "button": "bg-gradient-to-r from-emerald-600 to-teal-600 text-white",
            "button_hover": "hover:from-emerald-500 hover:to-teal-500",
            "heading": "text-emerald-300",
            "text": "text-emerald-200",
            "accent": "text-emerald-400",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-emerald-900/60",
            "button_shadow": "shadow-lg shadow-emerald-700/70",
            "hover_glow": "hover:shadow-emerald-500/40 hover:shadow-2xl",
            "transition": "transition-all duration-400 ease-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-2xl",
            "input": "rounded-xl",
         }
    },

    "rose_gold": {
        "name": "Rose Gold",
        "description": "Elegant, feminine, and luxurious — soft pinks with warm metallic undertones",
        "background": "bg-gradient-to-br from-rose-100 via-pink-100 to-amber-50",
        "colors": { 
            "surface": "bg-white/90 backdrop-blur-md",
            "card": "bg-white/95 backdrop-blur-lg border border-rose-200",
            "input": "bg-rose-50 border border-rose-300 text-rose-900 placeholder-rose-400",
            "button": "bg-gradient-to-r from-rose-500 to-pink-500 text-white",
            "button_hover": "hover:from-rose-600 hover:to-pink-600",
            "heading": "text-rose-800",
            "text": "text-rose-700",
            "accent": "text-rose-600",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-rose-200",
            "button_shadow": "shadow-xl shadow-rose-300",
            "hover_glow": "hover:shadow-2xl hover:shadow-rose-300/60",
            "transition": "transition-all duration-300 ease-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-full",
            "input": "rounded-2xl",
         }
    },

    "arctic_frost": {
        "name": "Arctic Frost",
        "description": "Crisp, minimalist light theme with icy cyan-blue touches and airy glass effects",
        "background": "bg-gradient-to-br from-slate-50 via-blue-50 to-cyan-50",
        "colors": { 
            "surface": "bg-white/80 backdrop-blur-xl",
            "card": "bg-white/90 backdrop-blur-2xl border border-cyan-200/50",
            "input": "bg-white/70 border border-cyan-300 text-slate-800 placeholder-slate-400",
            "button": "bg-gradient-to-r from-cyan-500 to-blue-600 text-white",
            "button_hover": "hover:from-cyan-400 hover:to-blue-500",
            "heading": "text-slate-800",
            "text": "text-slate-600",
            "accent": "text-cyan-600",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-cyan-100",
            "button_shadow": "shadow-lg shadow-cyan-200",
            "hover_glow": "hover:shadow-xl hover:shadow-cyan-300/50",
            "transition": "transition-all duration-300 ease-in-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-2xl",
            "input": "rounded-xl",
         }
    },

    "midnight_amber": {
        "name": "Midnight Amber",
        "description": "Warm, cozy dark theme with rich amber and bronze tones — like a high-end whiskey lounge",
        "background": "bg-gradient-to-br from-amber-950 via-orange-950 to-stone-950",
        "colors": {
            "surface": "bg-black/80 backdrop-blur-xl",
            "card": "bg-amber-950/90 backdrop-blur-2xl border border-amber-800/40",
            "input": "bg-amber-900/50 border border-amber-700 text-amber-200 placeholder-amber-500",
            "button": "bg-gradient-to-r from-amber-600 to-orange-600 text-white",
            "button_hover": "hover:from-amber-500 hover:to-orange-500",
            "heading": "text-amber-300",
            "text": "text-amber-200",
            "accent": "text-amber-400",
            },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-amber-900/60",
            "button_shadow": "shadow-xl shadow-amber-800/80",
            "hover_glow": "hover:shadow-amber-600/50 hover:shadow-2xl",
            "transition": "transition-all duration-500 ease-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-2xl",
            "input": "rounded-xl",
         }
    },

    "oceanic_deep": {
        "name": "Oceanic Deep",
        "description": "Immersive underwater feel with deep navy blues and glowing cyan highlights",
        "background": "bg-gradient-to-br from-[#001d3d] via-[#003366] to-[#000080]",
        "colors": { 
            "surface": "bg-[#0a1d37]/80 backdrop-blur-xl",
            "card": "bg-[#0f2b52]/80 backdrop-blur-2xl border border-cyan-800/30",
            "input": "bg-[#0f2b52]/60 border border-cyan-600/50 text-cyan-100 placeholder-cyan-500",
            "button": "bg-gradient-to-r from-cyan-600 via-blue-600 to-indigo-600 text-white",
            "button_hover": "hover:from-cyan-500 hover:via-blue-500 hover:to-indigo-500",
            "heading": "text-cyan-200",
            "text": "text-blue-200",
            "accent": "text-cyan-400",
         },
        "effects": { 
            "card_shadow": "shadow-2xl shadow-cyan-900/50",
            "button_shadow": "shadow-lg shadow-cyan-700/70",
            "hover_glow": "hover:shadow-[0_0_30px_rgba(34,211,238,0.5)]",
            "transition": "transition-all duration-400 ease-out",
         },
        "radius": { 
            "card": "rounded-3xl",
            "button": "rounded-2xl",
            "input": "rounded-xl",
         }
    }
}

def get_theme_replacements(theme_name: str) -> dict[str, str]:
    """
    Returns a dictionary mapping placeholder tokens to actual Tailwind classes.
    Example: "__THEME_CARD__" -> "bg-white/90 backdrop-blur-xl"
    """
    theme = THEMES.get(theme_name, THEMES["default"])
    
    # Flatten the theme structure into a single map
    replacements = {
        "__THEME_BACKGROUND__": theme["background"],
        
        "__THEME_SURFACE__": theme["colors"]["surface"],
        "__THEME_CARD__": theme["colors"]["card"],
        "__THEME_INPUT__": theme["colors"]["input"],
        "__THEME_BUTTON__": theme["colors"]["button"],
        "__THEME_BUTTON_HOVER__": theme["colors"]["button_hover"],
        "__THEME_HEADING__": theme["colors"]["heading"],
        "__THEME_TEXT__": theme["colors"]["text"],
        "__THEME_ACCENT__": theme["colors"]["accent"],
        
        "__THEME_CARD_SHADOW__": theme["effects"]["card_shadow"],
        "__THEME_BUTTON_SHADOW__": theme["effects"]["button_shadow"],
        "__THEME_HOVER_GLOW__": theme["effects"]["hover_glow"],
        "__THEME_TRANSITION__": theme["effects"]["transition"],
        
        "__THEME_RADIUS_CARD__": theme["radius"]["card"],
        "__THEME_RADIUS_BUTTON__": theme["radius"]["button"],
        "__THEME_RADIUS_INPUT__": theme["radius"]["input"],
    }
    
    return replacements