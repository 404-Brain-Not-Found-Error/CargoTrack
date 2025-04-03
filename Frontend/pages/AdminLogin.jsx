import { MainLoginHeader } from "../components/MainLoginHeader";
export default function Homepage() {
  return (
    <div>
      <header>
        <MainLoginHeader className="px-4 py-2 text-slate-900 font-semibold border-2 border-blue-600 hover:bg-blue-600 hover:text-white transition-all duration-300 rounded-lg shadow-sm hover:shadow-md">
          На главную
        </MainLoginHeader>
      </header>
      <main>
        <div className="mt-28 flex justify-center">LoginForm</div>
      </main>
    </div>
  );
}
