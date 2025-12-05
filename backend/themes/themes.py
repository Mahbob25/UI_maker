THEMES = {
    "default": {
        "name": "Default",
        "description": "Clean and professional light mode with subtle shadows and blue accents",
        "type": "light",
        "dynamic": "subtle-grain",
        "tokens": {
            "colors": {
                "primary": "#2563eb",       # blue-600
                "primary-foreground": "#ffffff",
                "secondary": "#f3f4f6",     # gray-100
                "secondary-foreground": "#1f2937", # gray-800
                "accent": "#3b82f6",        # blue-500
                "accent-foreground": "#ffffff",
                "background": "#f9fafb",    # gray-50
                "surface": "#ffffff",
                "surface-foreground": "#1f2937", # gray-800
                "muted": "#f3f4f6",         # gray-100
                "muted-foreground": "#6b7280",   # gray-500
                "border": "#e5e7eb",        # gray-200
                "input": "#ffffff",
                "ring": "#2563eb",          # blue-600
                "success": "#22c55e",       # green-500
                "warning": "#eab308",       # yellow-500
                "error": "#ef4444",         # red-500
            },
            "radius": {
                "sm": "0.375rem",
                "md": "0.5rem",
                "lg": "0.75rem",
                "xl": "1rem",
                "2xl": "1.5rem",
            },
            "shadows": {
                "sm": "0 1px 2px 0 rgba(0, 0, 0, 0.05)",
                "md": "0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",
                "lg": "0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)",
                "xl": "0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)",
                "glow": "0 0 20px rgba(37, 99, 235, 0.15)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #f9fafb 0%, #f3f4f6 100%)",
                "card": "linear-gradient(145deg, #ffffff 0%, #f9fafb 100%)",
                "primary": "linear-gradient(135deg, #3b82f6 0%, #2563eb 100%)",
                "accent": "linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%)"
            },
            "effects": {
                "backdropBlur": "12px",
                "grainOpacity": 0.02,
                "borderGlow": "0 0 10px rgba(37, 99, 235, 0.1)",
                "innerGlowIntensity": 0.05
            },
            "transitions": {
                "default": "all 0.2s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.2s cubic-bezier(0.4, 0, 0.2, 1), box-shadow 0.2s cubic-bezier(0.4, 0, 0.2, 1)",
                "colorShift": "background-color 0.3s ease, color 0.3s ease",
                "backgroundMove": "background-position 0.5s ease"
            }
        }
    },
    "nebula_dark": {
        "name": "Nebula Dark",
        "description": "Deep cosmic purple gradient with glowing glassmorphic cards",
        "type": "dark",
        "dynamic": "animated-stars",
        "tokens": {
            "colors": {
                "primary": "#6c63ff",
                "primary-foreground": "#ffffff",
                "secondary": "#2a2843",
                "secondary-foreground": "#e5e7eb",
                "accent": "#b9b4ff",
                "accent-foreground": "#0f0c29",
                "background": "#0f0c29",
                "surface": "#1b1a2e",
                "surface-foreground": "#e5e7eb",
                "muted": "#2a2843",
                "muted-foreground": "#9ca3af",
                "border": "#3a375a",
                "input": "#2a2843",
                "ring": "#6c63ff",
                "success": "#4ade80",
                "warning": "#facc15",
                "error": "#f87171",
            },
            "radius": {
                "sm": "0.5rem",
                "md": "0.75rem",
                "lg": "1rem",
                "xl": "1.5rem",
                "2xl": "2rem",
            },
            "shadows": {
                "sm": "0 0 8px rgba(108, 99, 255, 0.15)",
                "md": "0 0 20px rgba(108, 99, 255, 0.25)",
                "lg": "0 0 40px rgba(108, 99, 255, 0.35)",
                "xl": "0 0 60px rgba(108, 99, 255, 0.4)",
                "glow": "0 0 30px rgba(185, 180, 255, 0.5)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)",
                "card": "linear-gradient(145deg, rgba(27, 26, 46, 0.9) 0%, rgba(31, 29, 54, 0.8) 100%)",
                "primary": "linear-gradient(135deg, #6c63ff 0%, #5a52dd 100%)",
                "accent": "linear-gradient(135deg, #b9b4ff 0%, #8b85ff 100%)"
            },
            "effects": {
                "backdropBlur": "24px",
                "grainOpacity": 0.03,
                "borderGlow": "0 0 20px rgba(108, 99, 255, 0.3)",
                "innerGlowIntensity": 0.8
            },
            "transitions": {
                "default": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease",
                "colorShift": "background-color 0.4s ease, color 0.4s ease, box-shadow 0.4s ease",
                "backgroundMove": "background-position 1s ease-in-out"
            }
        }
    },
    "emerald_luxe": {
        "name": "Emerald Luxe",
        "description": "Sophisticated dark nature theme inspired by deep forests",
        "type": "dark",
        "dynamic": "gentle-wave",
        "tokens": {
            "colors": {
                "primary": "#059669",
                "primary-foreground": "#ffffff",
                "secondary": "#064e3b",
                "secondary-foreground": "#d1fae5",
                "accent": "#34d399",
                "accent-foreground": "#022c22",
                "background": "#022c22",
                "surface": "#064e3b",
                "surface-foreground": "#ecfdf5",
                "muted": "#065f46",
                "muted-foreground": "#6ee7b7",
                "border": "#047857",
                "input": "#065f46",
                "ring": "#10b981",
                "success": "#34d399",
                "warning": "#fbbf24",
                "error": "#f87171",
            },
            "radius": {
                "sm": "0.25rem",
                "md": "0.5rem",
                "lg": "1rem",
                "xl": "1.5rem",
                "2xl": "2rem",
            },
            "shadows": {
                "sm": "0 2px 8px rgba(5, 150, 105, 0.15)",
                "md": "0 8px 24px rgba(5, 150, 105, 0.25)",
                "lg": "0 16px 48px rgba(5, 150, 105, 0.35)",
                "xl": "0 24px 64px rgba(5, 150, 105, 0.4)",
                "glow": "0 0 40px rgba(52, 211, 153, 0.4)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #022c22 0%, #064e3b 50%, #065f46 100%)",
                "card": "linear-gradient(145deg, rgba(6, 78, 59, 0.7) 0%, rgba(6, 95, 70, 0.6) 100%)",
                "primary": "linear-gradient(135deg, #059669 0%, #047857 100%)",
                "accent": "linear-gradient(135deg, #34d399 0%, #10b981 100%)"
            },
            "effects": {
                "backdropBlur": "16px",
                "grainOpacity": 0.04,
                "borderGlow": "0 0 16px rgba(52, 211, 153, 0.3)",
                "innerGlowIntensity": 0.6
            },
            "transitions": {
                "default": "all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease",
                "colorShift": "background-color 0.5s ease, color 0.5s ease",
                "backgroundMove": "background-position 2s ease-in-out infinite"
            }
        }
    },
    "rose_gold": {
        "name": "Rose Gold",
        "description": "Elegant, feminine, and luxurious — soft pinks with warm metallic undertones",
        "type": "light",
        "dynamic": "sakura-petals",
        "tokens": {
            "colors": {
                "primary": "#f43f5e",
                "primary-foreground": "#ffffff",
                "secondary": "#ffe4e6",
                "secondary-foreground": "#881337",
                "accent": "#fb7185",
                "accent-foreground": "#ffffff",
                "background": "#fff1f2",
                "surface": "#ffffff",
                "surface-foreground": "#881337",
                "muted": "#ffe4e6",
                "muted-foreground": "#9f1239",
                "border": "#fda4af",
                "input": "#fff1f2",
                "ring": "#f43f5e",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#ef4444",
            },
            "radius": {
                "sm": "0.5rem",
                "md": "1rem",
                "lg": "1.5rem",
                "xl": "2rem",
                "2xl": "3rem",
            },
            "shadows": {
                "sm": "0 2px 8px rgba(244, 63, 94, 0.08)",
                "md": "0 8px 24px rgba(244, 63, 94, 0.12)",
                "lg": "0 16px 48px rgba(244, 63, 94, 0.18)",
                "xl": "0 24px 64px rgba(244, 63, 94, 0.22)",
                "glow": "0 0 32px rgba(251, 113, 133, 0.35)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #fff1f2 0%, #ffe4e6 50%, #fecdd3 100%)",
                "card": "linear-gradient(145deg, #ffffff 0%, #fff1f2 100%)",
                "primary": "linear-gradient(135deg, #fb7185 0%, #f43f5e 100%)",
                "accent": "linear-gradient(135deg, #fda4af 0%, #fb7185 100%)"
            },
            "effects": {
                "backdropBlur": "8px",
                "grainOpacity": 0.015,
                "borderGlow": "0 0 12px rgba(244, 63, 94, 0.15)",
                "innerGlowIntensity": 0.3
            },
            "transitions": {
                "default": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease",
                "colorShift": "background-color 0.4s ease, color 0.4s ease",
                "backgroundMove": "background-position 1.5s ease-in-out"
            }
        }
    },
    "arctic_frost": {
        "name": "Arctic Frost",
        "description": "Crisp, minimalist light theme with icy cyan-blue touches",
        "type": "light",
        "dynamic": "slow-floating-shapes",
        "tokens": {
            "colors": {
                "primary": "#06b6d4",
                "primary-foreground": "#ffffff",
                "secondary": "#ecfeff",
                "secondary-foreground": "#164e63",
                "accent": "#22d3ee",
                "accent-foreground": "#ffffff",
                "background": "#f0f9ff",
                "surface": "#ffffff",
                "surface-foreground": "#0e7490",
                "muted": "#cffafe",
                "muted-foreground": "#155e75",
                "border": "#67e8f9",
                "input": "#ffffff",
                "ring": "#06b6d4",
                "success": "#10b981",
                "warning": "#f59e0b",
                "error": "#ef4444",
            },
            "radius": {
                "sm": "0.25rem",
                "md": "0.5rem",
                "lg": "0.75rem",
                "xl": "1rem",
                "2xl": "1.5rem",
            },
            "shadows": {
                "sm": "0 2px 8px rgba(6, 182, 212, 0.08)",
                "md": "0 8px 24px rgba(6, 182, 212, 0.15)",
                "lg": "0 16px 48px rgba(6, 182, 212, 0.22)",
                "xl": "0 24px 64px rgba(6, 182, 212, 0.28)",
                "glow": "0 0 28px rgba(34, 211, 238, 0.4)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 50%, #dbeafe 100%)",
                "card": "linear-gradient(145deg, #ffffff 0%, #f0f9ff 100%)",
                "primary": "linear-gradient(135deg, #22d3ee 0%, #06b6d4 100%)",
                "accent": "linear-gradient(135deg, #67e8f9 0%, #22d3ee 100%)"
            },
            "effects": {
                "backdropBlur": "10px",
                "grainOpacity": 0.01,
                "borderGlow": "0 0 14px rgba(6, 182, 212, 0.2)",
                "innerGlowIntensity": 0.25
            },
            "transitions": {
                "default": "all 0.25s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease",
                "colorShift": "background-color 0.35s ease, color 0.35s ease",
                "backgroundMove": "background-position 3s ease-in-out infinite alternate"
            }
        }
    },
    "midnight_amber": {
        "name": "Midnight Amber",
        "description": "Warm, cozy dark theme with rich amber and bronze tones",
        "type": "dark",
        "dynamic": "subtle-grain",
        "tokens": {
            "colors": {
                "primary": "#d97706",
                "primary-foreground": "#ffffff",
                "secondary": "#451a03",
                "secondary-foreground": "#fef3c7",
                "accent": "#f59e0b",
                "accent-foreground": "#000000",
                "background": "#292524",
                "surface": "#1c1917",
                "surface-foreground": "#fef3c7",
                "muted": "#44403c",
                "muted-foreground": "#a8a29e",
                "border": "#78350f",
                "input": "#292524",
                "ring": "#d97706",
                "success": "#22c55e",
                "warning": "#f59e0b",
                "error": "#ef4444",
            },
            "radius": {
                "sm": "0.25rem",
                "md": "0.5rem",
                "lg": "0.75rem",
                "xl": "1rem",
                "2xl": "1.5rem",
            },
            "shadows": {
                "sm": "0 2px 8px rgba(217, 119, 6, 0.15)",
                "md": "0 8px 24px rgba(217, 119, 6, 0.25)",
                "lg": "0 16px 48px rgba(217, 119, 6, 0.35)",
                "xl": "0 24px 64px rgba(217, 119, 6, 0.45)",
                "glow": "0 0 36px rgba(245, 158, 11, 0.5)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #292524 0%, #1c1917 50%, #0c0a09 100%)",
                "card": "linear-gradient(145deg, rgba(28, 25, 23, 0.95) 0%, rgba(68, 64, 60, 0.8) 100%)",
                "primary": "linear-gradient(135deg, #f59e0b 0%, #d97706 100%)",
                "accent": "linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%)"
            },
            "effects": {
                "backdropBlur": "14px",
                "grainOpacity": 0.08,
                "borderGlow": "0 0 18px rgba(217, 119, 6, 0.35)",
                "innerGlowIntensity": 0.7
            },
            "transitions": {
                "default": "all 0.5s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.5s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.5s ease",
                "colorShift": "background-color 0.6s ease, color 0.6s ease",
                "backgroundMove": "background-position 1.2s ease-in-out"
            }
        }
    },
    "oceanic_deep": {
        "name": "Oceanic Deep",
        "description": "Immersive underwater feel with deep navy blues and glowing cyan highlights",
        "type": "dark",
        "dynamic": "hue-shift",
        "tokens": {
            "colors": {
                "primary": "#0ea5e9",
                "primary-foreground": "#ffffff",
                "secondary": "#0c4a6e",
                "secondary-foreground": "#e0f2fe",
                "accent": "#38bdf8",
                "accent-foreground": "#082f49",
                "background": "#020617",
                "surface": "#0f172a",
                "surface-foreground": "#f1f5f9",
                "muted": "#1e293b",
                "muted-foreground": "#94a3b8",
                "border": "#1e293b",
                "input": "#0f172a",
                "ring": "#0ea5e9",
                "success": "#22c55e",
                "warning": "#f59e0b",
                "error": "#ef4444",
            },
            "radius": {
                "sm": "0.375rem",
                "md": "0.5rem",
                "lg": "0.75rem",
                "xl": "1rem",
                "2xl": "1.5rem",
            },
            "shadows": {
                "sm": "0 2px 8px rgba(14, 165, 233, 0.12)",
                "md": "0 8px 24px rgba(14, 165, 233, 0.22)",
                "lg": "0 16px 48px rgba(14, 165, 233, 0.32)",
                "xl": "0 24px 64px rgba(14, 165, 233, 0.42)",
                "glow": "0 0 40px rgba(56, 189, 248, 0.5)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #020617 0%, #0c4a6e 50%, #075985 100%)",
                "card": "linear-gradient(145deg, rgba(15, 23, 42, 0.9) 0%, rgba(30, 41, 59, 0.8) 100%)",
                "primary": "linear-gradient(135deg, #38bdf8 0%, #0ea5e9 100%)",
                "accent": "linear-gradient(135deg, #7dd3fc 0%, #38bdf8 100%)"
            },
            "effects": {
                "backdropBlur": "20px",
                "grainOpacity": 0.05,
                "borderGlow": "0 0 24px rgba(14, 165, 233, 0.4)",
                "innerGlowIntensity": 0.85
            },
            "transitions": {
                "default": "all 0.4s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.4s ease",
                "colorShift": "background-color 0.8s ease, color 0.8s ease, filter 0.8s ease",
                "backgroundMove": "background-position 4s ease-in-out infinite alternate"
            }
        }
    },
    "sunrise": {
        "name": "Sunrise",
        "description": "Warm, uplifting gradient of orange, rose, and purple — like watching dawn from your desk",
        "type": "light",
        "dynamic": "moving-gradient",
        "tokens": {
            "colors": {
                "primary": "#f97316",
                "primary-foreground": "#ffffff",
                "secondary": "#fed7aa",
                "secondary-foreground": "#7c2d12",
                "accent": "#fb923c",
                "accent-foreground": "#ffffff",
                "background": "#fff7ed",
                "surface": "#ffffff",
                "surface-foreground": "#9a3412",
                "muted": "#ffedd5",
                "muted-foreground": "#c2410c",
                "border": "#fdba74",
                "input": "#ffffff",
                "ring": "#f97316",
                "success": "#22c55e",
                "warning": "#eab308",
                "error": "#ef4444",
            },
            "radius": {
                "sm": "0.375rem",
                "md": "0.5rem",
                "lg": "0.75rem",
                "xl": "1rem",
                "2xl": "1.5rem",
            },
            "shadows": {
                "sm": "0 2px 8px rgba(249, 115, 22, 0.1)",
                "md": "0 8px 24px rgba(249, 115, 22, 0.15)",
                "lg": "0 16px 48px rgba(249, 115, 22, 0.22)",
                "xl": "0 24px 64px rgba(249, 115, 22, 0.28)",
                "glow": "0 0 32px rgba(251, 146, 60, 0.4)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #fff7ed 0%, #fed7aa 25%, #fda4af 75%, #e9d5ff 100%)",
                "card": "linear-gradient(145deg, #ffffff 0%, #fff7ed 100%)",
                "primary": "linear-gradient(135deg, #fb923c 0%, #f97316 100%)",
                "accent": "linear-gradient(135deg, #fdba74 0%, #fb923c 100%)"
            },
            "effects": {
                "backdropBlur": "8px",
                "grainOpacity": 0.02,
                "borderGlow": "0 0 16px rgba(249, 115, 22, 0.2)",
                "innerGlowIntensity": 0.4
            },
            "transitions": {
                "default": "all 0.3s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.3s ease",
                "colorShift": "background-color 0.5s ease, color 0.5s ease",
                "backgroundMove": "background-position 10s ease-in-out infinite alternate"
            }
        }
    },
    "cyber_neon": {
        "name": "Cyber Neon",
        "description": "Intense synthwave cyberpunk vibe with electric cyan-purple glows and retro-futuristic energy",
        "type": "dark",
        "dynamic": "scanlines",
        "tokens": {
            "colors": {
                "primary": "#a855f7",
                "primary-foreground": "#ffffff",
                "secondary": "#1a0033",
                "secondary-foreground": "#e9d5ff",
                "accent": "#06b6d4",
                "accent-foreground": "#ffffff",
                "background": "#0a0028",
                "surface": "#120030",
                "surface-foreground": "#e0e7ff",
                "muted": "#1a0a3e",
                "muted-foreground": "#a78bfa",
                "border": "#7c3aed",
                "input": "#1a0a3e",
                "ring": "#a855f7",
                "success": "#10b981",
                "warning": "#fbbf24",
                "error": "#f87171",
            },
            "radius": {
                "sm": "0.25rem",
                "md": "0.375rem",
                "lg": "0.5rem",
                "xl": "0.75rem",
                "2xl": "1rem",
            },
            "shadows": {
                "sm": "0 0 8px rgba(168, 85, 247, 0.3), 0 0 4px rgba(6, 182, 212, 0.2)",
                "md": "0 0 16px rgba(168, 85, 247, 0.5), 0 0 8px rgba(6, 182, 212, 0.3)",
                "lg": "0 0 32px rgba(168, 85, 247, 0.6), 0 0 16px rgba(6, 182, 212, 0.4)",
                "xl": "0 0 48px rgba(168, 85, 247, 0.7), 0 0 24px rgba(6, 182, 212, 0.5)",
                "glow": "0 0 40px rgba(6, 182, 212, 0.8), 0 0 20px rgba(168, 85, 247, 0.6)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #0a0028 0%, #1a0033 50%, #2d0055 100%)",
                "card": "linear-gradient(145deg, rgba(18, 0, 48, 0.8) 0%, rgba(26, 10, 62, 0.7) 100%)",
                "primary": "linear-gradient(135deg, #06b6d4 0%, #a855f7 100%)",
                "accent": "linear-gradient(135deg, #22d3ee 0%, #c084fc 100%)"
            },
            "effects": {
                "backdropBlur": "16px",
                "grainOpacity": 0.06,
                "borderGlow": "0 0 20px rgba(168, 85, 247, 0.5), 0 0 10px rgba(6, 182, 212, 0.3)",
                "innerGlowIntensity": 1.0
            },
            "transitions": {
                "default": "all 0.25s cubic-bezier(0.4, 0, 0.2, 1)",
                "hoverLift": "transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1), box-shadow 0.25s ease, filter 0.25s ease",
                "colorShift": "background-color 0.3s ease, color 0.3s ease, box-shadow 0.3s ease",
                "backgroundMove": "background-position 0.8s ease-in-out"
            }
        }
    },
    "terminal_green": {
        "name": "Terminal Green",
        "description": "Classic hacker terminal aesthetic with phosphor green glow on deep black",
        "type": "dark",
        "dynamic": "scanlines",
        "tokens": {
            "colors": {
                "primary": "#00ff41",
                "primary-foreground": "#000000",
                "secondary": "#001a00",
                "secondary-foreground": "#00ff41",
                "accent": "#00cc33",
                "accent-foreground": "#000000",
                "background": "#000000",
                "surface": "#0a0a0a",
                "surface-foreground": "#00ff41",
                "muted": "#001a00",
                "muted-foreground": "#009929",
                "border": "#00cc33",
                "input": "#0a0a0a",
                "ring": "#00ff41",
                "success": "#00ff41",
                "warning": "#ffff00",
                "error": "#ff0000",
            },
            "radius": {
                "sm": "0.125rem",
                "md": "0.25rem",
                "lg": "0.375rem",
                "xl": "0.5rem",
                "2xl": "0.75rem",
            },
            "shadows": {
                "sm": "0 0 8px rgba(0, 255, 65, 0.4)",
                "md": "0 0 16px rgba(0, 255, 65, 0.6)",
                "lg": "0 0 32px rgba(0, 255, 65, 0.7)",
                "xl": "0 0 48px rgba(0, 255, 65, 0.8)",
                "glow": "0 0 40px rgba(0, 255, 65, 0.9), 0 0 20px rgba(0, 255, 65, 0.6)"
            },
            "gradients": {
                "background": "linear-gradient(135deg, #000000 0%, #001a00 100%)",
                "card": "linear-gradient(145deg, rgba(10, 10, 10, 0.95) 0%, rgba(0, 26, 0, 0.8) 100%)",
                "primary": "linear-gradient(135deg, #00ff41 0%, #00cc33 100%)",
                "accent": "linear-gradient(135deg, #00cc33 0%, #009929 100%)"
            },
            "effects": {
                "backdropBlur": "4px",
                "grainOpacity": 0.07,
                "borderGlow": "0 0 16px rgba(0, 255, 65, 0.6)",
                "innerGlowIntensity": 0.9
            },
            "transitions": {
                "default": "all 0.15s linear",
                "hoverLift": "transform 0.15s linear, box-shadow 0.15s linear, text-shadow 0.15s linear",
                "colorShift": "background-color 0.2s linear, color 0.2s linear",
                "backgroundMove": "background-position 0.5s linear"
            }
        }
    },
    "ai_creative": {
        "name": "AI Creative",
        "description": "Let the AI design a unique, custom theme for you",
        "type": "custom",
        "dynamic": "ai-generated",
        "tokens": {}
    }
}

def generate_theme_css(theme_name: str) -> str:
    """
    Generates the CSS variables for the selected theme.
    """
    if theme_name == "ai_creative":
        return "/* AI Creative Theme: Styles will be generated by the LLM */"

    theme = THEMES.get(theme_name, THEMES["default"])
    tokens = theme["tokens"]
    
    css_lines = [":root {"]
    
    # Colors
    for key, value in tokens["colors"].items():
        css_lines.append(f"  --color-{key}: {value};")
        
    # Radius
    for key, value in tokens["radius"].items():
        css_lines.append(f"  --radius-{key}: {value};")
    
    # Shadows
    if "shadows" in tokens:
        for key, value in tokens["shadows"].items():
            css_lines.append(f"  --shadow-{key}: {value};")
    
    # Gradients
    if "gradients" in tokens:
        for key, value in tokens["gradients"].items():
            css_lines.append(f"  --gradient-{key}: {value};")
    
    # Effects
    if "effects" in tokens:
        for key, value in tokens["effects"].items():
            css_lines.append(f"  --effect-{key}: {value};")
    
    # Transitions
    if "transitions" in tokens:
        for key, value in tokens["transitions"].items():
            css_lines.append(f"  --transition-{key}: {value};")
        
    css_lines.append("}")
    return "\n".join(css_lines)

def get_theme_replacements(theme_name: str) -> dict[str, str]:
    """
    Legacy support for direct replacements, but now we prefer CSS variables.
    This can be deprecated or adapted to return the semantic class names.
    """
    return {}