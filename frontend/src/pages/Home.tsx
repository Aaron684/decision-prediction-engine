import { useNavigate } from "react-router-dom";

import PageLayout from "../components/layout/PageLayout";
import Card from "../components/ui/Card";
import Button from "../components/ui/Button";

function Home() {
  const navigate = useNavigate();

  return (
    <PageLayout>
      <Card>
        <h1 className="text-4xl font-bold text-slate-800">Welcome</h1>

        <p className="mt-4 text-slate-600">
          Build prediction models from your own historical decisions.
        </p>

        <div className="mt-8 flex gap-4">
          <Button onClick={() => navigate("/categories")}>
            View Categories
          </Button>

          <Button onClick={() => navigate("/help")}>Learn More</Button>
        </div>
      </Card>
    </PageLayout>
  );
}

export default Home;
