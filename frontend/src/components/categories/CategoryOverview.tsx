import type { Category } from "../../api/Categories";

import Card from "../ui/Card";

interface CategoryOverviewProps {
  category: Category;
}

function CategoryOverview({ category }: CategoryOverviewProps) {
  return (
    <Card>
      <div className="space-y-5">
        <div>
          <p className="text-sm text-slate-500">Description</p>

          <p className="mt-1 text-slate-700">{category.description}</p>
        </div>

        <div className="grid grid-cols-2 gap-6">
          <div>
            <p className="text-sm text-slate-500">Prediction Type</p>

            <p className="mt-1 font-semibold text-slate-800">
              {formatTargetType(category.target_type)}
            </p>
          </div>

          <div>
            <p className="text-sm text-slate-500">Target</p>

            <p className="mt-1 font-semibold text-slate-800">
              {category.target_name}
            </p>
          </div>
        </div>
      </div>
    </Card>
  );
}

function formatTargetType(targetType: string) {
  return targetType.charAt(0).toUpperCase() + targetType.slice(1);
}

export default CategoryOverview;
