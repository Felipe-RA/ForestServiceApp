module.exports = {
  testEnvironment: 'jsdom',
  testPathIgnorePatterns: ['/node_modules/', '/.next/'],
  transform: {
    '^.+\\.(js|jsx|ts|tsx)$': '<rootDir>/node_modules/babel-jest',
  },
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  collectCoverageFrom: [
    "app/**/*.tsx", // Collect coverage from .tsx files under the app folder
    "!app/**/*.d.ts", // Exclude TypeScript declaration files
    // Add other patterns to exclude files as needed
  ],
  coverageDirectory: "<rootDir>/coverage", // The directory where Jest should output coverage files
  coverageReporters: ["json", "lcov", "text", "clover"], // Reporters you want Jest to use
  coveragePathIgnorePatterns: [
    "/node_modules/",
    "<rootDir>/__tests__/", // Exclude test files themselves from coverage
    "<rootDir>/pages/_app.js",
    "<rootDir>/pages/_document.js",
    // Add other paths to ignore here if needed
  ],
};
