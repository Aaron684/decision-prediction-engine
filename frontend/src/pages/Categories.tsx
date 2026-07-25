import { useNavigate } from "react-router-dom";

import PageLayout from "../components/layout/PageLayout";
import PageHeader from "../components/layout/PageHeader";
import CategoryCard from "../components/categories/CategoryCard";
import Card from "../components/ui/Card";
import Button from "../components/ui/Button";

function Categories() {
  const navigate = useNavigate();

  // Temporary mock data until backend integration
  const categories = [
    {
      id: 1,
      name: "Should I Accept This Job?",
      type: "Classification",
      features: 5,
      observations: 120,
    },
    {
      id: 2,
      name: "Should I Buy This House?",
      type: "Regression",
      features: 8,
      observations: 58,
    },
  ];

  return (
    <PageLayout>
      <PageHeader
        title="Categories"
        subtitle="Manage your prediction problems."
      />

      <div className="mb-6 flex justify-end">
        <Button
          onClick={() => {
            // We'll replace this later with the create page.
            console.log("Create Category");
          }}
        >
          + New Category
        </Button>
      </div>

      {categories.length === 0 ? (
        <Card>
          <div className="py-10 text-center">
            <h2 className="text-2xl font-semibold text-slate-800">
              No Categories Yet
            </h2>

            <p className="mt-3 text-slate-600">
              Create your first prediction problem to begin training machine
              learning models.
            </p>

            <div className="mt-8">
              <Button
                onClick={() => {
                  console.log("Create Category");
                }}
              >
                Create Your First Category
              </Button>
            </div>
          </div>
        </Card>
      ) : (
        <div className="space-y-4">
          {categories.map((category) => (
            <CategoryCard
              key={category.id}
              name={category.name}
              type={category.type}
              features={category.features}
              observations={category.observations}
              onOpen={() => navigate(`/categories/${category.id}`)}
            />
          ))}
        </div>
      )}
    </PageLayout>
  );
}

export default Categories;
