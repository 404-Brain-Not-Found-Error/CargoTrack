import Link from "next/link";

export function LoginChoose() {
  return (
    <div className="min-h-screen flex flex-col items-center bg-gray-50 py-12 px-4 sm:px-6 lg:px-8">
      <h1 className="text-4xl font-bold text-gray-900 mb-8 mt-24">Войти как</h1>
      <div className="w-full max-w-md bg-white rounded-xl shadow-2xl p-8 space-y-4 transition-all duration-300">
        <div className="grid grid-cols-1 gap-6">
          <Link href="/ClientLoginPage">
            <button className="w-full py-6 px-10 text-2xl bg-[#3D55F9] text-white font-bold rounded-lg shadow-md hover:bg-[#2c3eb8] transition-all duration-300 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-[#3D55F9] focus:ring-opacity-50">
              Клиент
            </button>
          </Link>
          <Link href="/AdminLoginPage">
            <button className="w-full py-3 px-6 bg-[#3D55F9] text-white text-lg font-semibold rounded-lg shadow-md hover:bg-[#2c3eb8] transition-all duration-300 hover:shadow-lg focus:outline-none focus:ring-2 focus:ring-[#3D55F9] focus:ring-opacity-50">
              Сотрудник
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
}
