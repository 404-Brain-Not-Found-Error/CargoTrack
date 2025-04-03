import { MainLoginHeader } from "../components/MainLoginHeader";
import { LoginChoose } from "../components/LoginChoose";

export default function Homepage() {
  return (
    <div>
      <header><MainLoginHeader /></header>
      <main><LoginChoose></LoginChoose></main>
    </div>
  );
}
