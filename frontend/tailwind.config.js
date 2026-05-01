/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "on-tertiary-fixed": "#311400",
        "surface-container": "#e7eefe",
        "surface": "#f9f9ff",
        "surface-variant": "#dce2f3",
        "primary-container": "#2170e4",
        "surface-tint": "#005ac2",
        "on-primary-container": "#fefcff",
        "primary": "#0058be",
        "tertiary-container": "#b75b00",
        "on-surface-variant": "#424754",
        "on-error": "#ffffff",
        "tertiary-fixed": "#ffdcc6",
        "outline-variant": "#c2c6d6",
        "on-secondary-fixed-variant": "#304671",
        "on-background": "#151c27",
        "background": "#f9f9ff",
        "secondary-fixed-dim": "#b1c6f9",
        "on-surface": "#151c27",
        "surface-bright": "#f9f9ff",
        "on-primary": "#ffffff",
        "surface-container-lowest": "#ffffff",
        "secondary-fixed": "#d8e2ff",
        "outline": "#727785",
        "secondary": "#495e8a",
        "on-tertiary-fixed-variant": "#723600",
        "inverse-surface": "#2a313d",
        "on-secondary": "#ffffff",
        "surface-dim": "#d3daea",
        "on-secondary-fixed": "#001a42",
        "on-error-container": "#93000a",
        "error-container": "#ffdad6",
        "surface-container-high": "#e2e8f8",
        "error": "#ba1a1a",
        "inverse-on-surface": "#ebf1ff",
        "on-secondary-container": "#405682",
        "secondary-container": "#b6ccff",
        "inverse-primary": "#adc6ff",
        "tertiary-fixed-dim": "#ffb786",
        "surface-container-low": "#f0f3ff",
        "on-tertiary": "#ffffff",
        "primary-fixed": "#d8e2ff",
        "on-tertiary-container": "#fffbff",
        "surface-container-highest": "#dce2f3",
        "primary-fixed-dim": "#adc6ff",
        "on-primary-fixed-variant": "#004395",
        "on-primary-fixed": "#001a42",
        "tertiary": "#924700"
      },
      borderRadius: {
        "DEFAULT": "0.25rem",
        "lg": "0.5rem",
        "xl": "0.75rem",
        "full": "9999px"
      },
      fontFamily: {
        "headline": ["Inter"],
        "display": ["Inter"],
        "body": ["Inter"],
        "label": ["Inter"]
      },
      boxShadow: {
        "wash": "0 12px 40px rgba(21, 28, 39, 0.06)"
      }
    },
  },
  plugins: [],
}
