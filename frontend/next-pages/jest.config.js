module.exports = {
    testEnvironment: 'jsdom',
    testPathIgnorePatterns: ['/node_modules/', '/.next/'],
    transform: {
      '^.+\\.(js|jsx|ts|tsx)$': '<rootDir>/node_modules/babel-jest',
    },
    setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
    collectCoverageFrom: [ // Define the files Jest should collect coverage from
    "app/**/*.tsx", // get source files from app
    "!app/**/*.d.ts", // exclude TypeScript declaration files
    // add more patterns as needed
    ],
    coveragePathIgnorePatterns: [
      "/node_modules/",
      "<rootDir>/__tests__/",
      "<rootDir>/pages/_app.js",
      "<rootDir>/pages/_document.js",
      // Add other paths to ignore here if we need them
    ],
  };
  