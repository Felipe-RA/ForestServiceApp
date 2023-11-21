module.exports = {
    testEnvironment: 'jsdom',
    testPathIgnorePatterns: ['/node_modules/', '/.next/'],
    transform: {
      '^.+\\.(js|jsx|ts|tsx)$': '<rootDir>/node_modules/babel-jest',
    },
    coveragePathIgnorePatterns: [
        "/node_modules/",
        "<rootDir>/__tests__/",
        "<rootDir>/pages/_app.js",
        "<rootDir>/pages/_document.js",
        // we will put here more ignore patterns here, if needed
      ],
  };
