import { render, screen } from '@testing-library/react';
import App from './App';

describe('App', () => {
  it('renders the main application container', () => {
    render(<App />);
    const mainContainer = screen.getByRole('main');
    expect(mainContainer).toBeInTheDocument();
  });
});
