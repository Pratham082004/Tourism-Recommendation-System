/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'brand-pink': '#ff4785',
        'brand-pink-dark': '#e03a6f',
        'brand-blue': '#4c84ff',
        'bg-light': '#f8f9fc',
      }
    },
  },
  plugins: [],
}
