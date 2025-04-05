import { useState } from "react";
import { FaEye, FaEyeSlash } from "react-icons/fa";

export default function Login() {
  const [showPassword, setShowPassword] = useState(false);

  return (
    <form>
      <div className="flex flex-col items-center space-y-6 bg-gradient-to-br from-blue-500 to-blue-600 shadow-2xl rounded-xl p-10 max-w-sm mx-auto mt-10">
        <h2 className="text-3xl font-bold text-white mb-6">Вход</h2>
        <input
          type="text"
          placeholder="Ваш email"
          className="border-2 border-gray-200 rounded-lg p-3 w-full max-w-xs focus:outline-none focus:border-blue-300 focus:ring-2 focus:ring-blue-200 transition-all duration-200"
          required
        />
        <div className="relative w-full max-w-xs">
          <input
            type={showPassword ? "text" : "password"}
            placeholder="Пароль"
            className="border-2 border-gray-200 rounded-lg p-3 w-full focus:outline-none focus:border-blue-300 focus:ring-2 focus:ring-blue-200 transition-all duration-200"
            required
          />
          <button
            type="button"
            onClick={() => setShowPassword((prev) => !prev)}
            className="absolute right-3 top-1/2 transform -translate-y-1/2 text-gray-500 hover:text-gray-700"
          >
            {showPassword ? <FaEye /> : <FaEyeSlash />}
          </button>
        </div>
        <button
          type="submit"
          className="bg-white text-blue-700 font-bold py-3 px-6 rounded-lg hover:transform hover:scale-105 transition-all duration-200 shadow-md w-full max-w-xs"
        >
          Войти
        </button>
      </div>
    </form>
  );
}
