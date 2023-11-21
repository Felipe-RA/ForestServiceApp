module.exports = {
    testEnvironment: 'jsdom',
    testPathIgnorePatterns: ['/node_modules/', '/.next/'],
    transform: {
      '^.+\\.(js|jsx|ts|tsx)$': '<rootDir>/node_modules/babel-jest',
    },
    setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
    coveragePathIgnorePatterns: [
      "/node_modules/",
      "<rootDir>/__tests__/",
      "<rootDir>/pages/_app.js",
      "<rootDir>/pages/_document.js",
      // Add other paths to ignore here if we need them
    ],
  };
  