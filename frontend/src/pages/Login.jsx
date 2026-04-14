'''import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { login } from '../services/api';

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');
        try {
            const data = await login(email, password);
            localStorage.setItem('token', data.access_token);
            navigate('/');
        } catch (err) {
            setError('Invalid email or password');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="bg-surface font-body text-on-surface overflow-hidden">
            <div className="fixed inset-0 z-0">
                <div className="absolute inset-0 bg-primary-container opacity-95"></div>
                <img
                    className="w-full h-full object-cover opacity-30 mix-blend-overlay"
                    data-alt="cinematic long exposure of city traffic at night with blurred streaks of yellow taxi lights against deep blue architecture"
                    src="https://lh3.googleusercontent.com/aida-public/AB6AXuAU87f2jpJ4Y8jrt51G-F-pRs4a4yCWc7qV9rS2eA6nJNm9R1-lE7WJPbyj-wo3X0g2zrtC40L-LU3gem68jEaotdoxm7xc7jAE_E614nfUopQAIW3VuN1XTsp_K_-G2Gh4pOrZ6IGspoCzvaM0F2vXXTX037cl4EvQrzkKT4FVFjx6FTn9jH7t5o2dTYuyPaqcmCQ5NLibbGVJsVyOakDWdg0YN9Tq77aAA6b5BwIOxXwAl1prYiqzmKW1qDQ0mZllWO6qTW8lSlrF"
                />
                <div className="absolute inset-0 bg-gradient-to-tr from-primary via-transparent to-transparent opacity-60"></div>
            </div>
            <main className="relative z-10 flex min-h-screen items-center justify-center p-6">
                <div className="flex w-full max-w-6xl items-stretch gap-8">
                    <div className="hidden lg:flex flex-col justify-between w-1/2 p-12 text-on-primary">
                        <div className="space-y-4">
                            <div className="flex items-center gap-3">
                                <div className="w-12 h-12 bg-tertiary-fixed-dim flex items-center justify-center rounded-xl">
                                    <span className="material-symbols-outlined text-primary text-3xl" style={{ fontVariationSettings: "'FILL' 1" }}>local_taxi</span>
                                </div>
                                <h1 className="font-headline text-3xl font-extrabold tracking-tight">Kinetic Fleet</h1>
                            </div>
                            <h2 className="text-5xl font-headline font-extrabold leading-tight mt-12">
                                Precision <br />
                                <span className="text-tertiary-fixed-dim">Command</span> for <br />
                                Modern Logistics.
                            </h2>
                            <p className="text-on-primary-container text-lg max-w-md mt-6">
                                Experience the authority of fleet management through an interface designed for clarity, speed, and luxury.
                            </p>
                        </div>
                        <div className="flex items-center gap-6 py-8">
                            <div className="flex items-center gap-2">
                                <div className="w-3 h-3 rounded-full bg-tertiary-fixed-dim blur-[2px]"></div>
                                <span className="text-xs font-label uppercase tracking-widest opacity-70">1,204 Active Units</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <div className="w-3 h-3 rounded-full bg-green-400 blur-[2px]"></div>
                                <span className="text-xs font-label uppercase tracking-widest opacity-70">System Optimal</span>
                            </div>
                        </div>
                    </div>
                    <div className="w-full lg:w-1/2 flex items-center justify-center">
                        <div className="w-full max-w-md bg-surface-container-lowest rounded-xl p-10 ambient-shadow border border-outline-variant/10">
                            <div className="lg:hidden flex flex-col items-center mb-8">
                                <div className="w-10 h-10 bg-tertiary-fixed-dim flex items-center justify-center rounded-lg mb-4">
                                    <span className="material-symbols-outlined text-primary text-2xl" style={{ fontVariationSettings: "'FILL' 1" }}>local_taxi</span>
                                </div>
                                <h1 className="font-headline text-2xl font-bold text-primary">Kinetic Fleet</h1>
                            </div>
                            <div className="mb-10 text-center lg:text-left">
                                <h3 className="text-2xl font-headline font-extrabold text-on-background">Welcome Back</h3>
                                <p className="text-on-surface-variant mt-2">Access the command dashboard</p>
                            </div>
                            <form className="space-y-6" onSubmit={handleSubmit}>
                                <div className="space-y-2">
                                    <label className="block text-sm font-semibold text-on-surface ml-1" htmlFor="email">Email Address</label>
                                    <div className="relative group">
                                        <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                            <span className="material-symbols-outlined text-outline text-xl">alternate_email</span>
                                        </div>
                                        <input
                                            className="block w-full pl-11 pr-4 py-4 bg-surface-container-low border-0 rounded-xl text-on-surface placeholder-outline focus:ring-2 focus:ring-primary/20 transition-all duration-200"
                                            id="email"
                                            name="email"
                                            placeholder="name@kinetic.authority"
                                            type="email"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                        />
                                    </div>
                                </div>
                                <div className="space-y-2">
                                    <div className="flex justify-between items-center px-1">
                                        <label className="text-sm font-semibold text-on-surface" htmlFor="password">Password</label>
                                        <Link className="text-xs font-semibold text-primary hover:text-surface-tint transition-colors" to="#">Forgot Password?</Link>
                                    </div>
                                    <div className="relative group">
                                        <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
                                            <span className="material-symbols-outlined text-outline text-xl">lock_open</span>
                                        </div>
                                        <input
                                            className="block w-full pl-11 pr-4 py-4 bg-surface-container-low border-0 rounded-xl text-on-surface placeholder-outline focus:ring-2 focus:ring-primary/20 transition-all duration-200"
                                            id="password"
                                            name="password"
                                            placeholder="••••••••••••"
                                            type="password"
                                            value={password}
                                            onChange={(e) => setPassword(e.target..value)}
                                        />
                                    </div>
                                </div>
                                {error && <p className="text-red-500 text-sm">{error}</p>}
                                <button
                                    className="group relative w-full flex justify-center py-4 px-4 border border-transparent rounded-xl text-primary font-bold bg-tertiary-fixed-dim hover:bg-opacity-90 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-tertiary-fixed-dim transition-all duration-300"
                                    type="submit"
                                    disabled={loading}
                                >
                                    <span className="absolute left-0 inset-y-0 flex items-center pl-4 opacity-0 group-hover:opacity-100 transition-opacity">
                                        <span className="material-symbols-outlined text-xl">arrow_forward</span>
                                    </span>
                                    {loading ? 'Logging in...' : 'Login to Dashboard'}
                                </button>
                            </form>
                            <div className="mt-12 text-center">
                                <p className="text-sm text-on-surface-variant font-medium">
                                    Don't have an account?
                                    <Link className="text-primary font-bold hover:underline underline-offset-4 ml-1" to="#">Sign Up</Link>
                                </p>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
            <footer className="fixed bottom-0 left-0 w-full p-8 z-10 hidden lg:block">
                <div className="max-w-7xl mx-auto flex justify-between items-center opacity-60">
                    <div className="flex gap-8">
                        <Link className="text-xs font-semibold text-on-primary-fixed uppercase tracking-widest hover:text-tertiary-fixed-dim transition-colors" to="#">Privacy Policy</Link>
                        <Link className="text-xs font-semibold text-on-primary-fixed uppercase tracking-widest hover:text-tertiary-fixed-dim transition-colors" to="#">Terms of Service</Link>
                        <Link className="text-xs font-semibold text-on-primary-fixed uppercase tracking-widest hover:text-tertiary-fixed-dim transition-colors" to="#">Support</Link>
                    </div>
                    <p className="text-xs font-semibold text-on-primary-fixed uppercase tracking-widest">
                        © 2024 Kinetic Authority Cab Management.
                    </p>
                </div>
            </footer>
        </div>
    );
};

export default Login;
''