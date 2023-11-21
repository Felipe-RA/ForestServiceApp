// frontend/next-pages/__tests__/AreCoveragesWorking.test.tsx

import { render, screen } from '@testing-library/react';
import AreCoveragesWorking from '../app/AreCoveragesWorking';

test('renders AreCoveragesWorking component', () => {
  render(<AreCoveragesWorking />);
  const textElement = screen.getByText(/AreCoveragesWorking, AreCoveragesWorking!/i);
  expect(textElement).toBeInTheDocument();
});
