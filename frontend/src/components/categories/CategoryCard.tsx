import Card from "../ui/Card";
import Button from "../ui/Button";

interface CategoryCardProps {
  name: string;
  type: string;
  features: number;
  observations: number;
  onOpen?: () => void;
}

function CategoryCard({
  name,
  type,
  features,
  observations,
  onOpen,
}: CategoryCardProps) {
  return (
    <Card>
      <div className="flex items-start justify-between">
        <div>
          <h2 className="text-xl font-semibold text-slate-800">{name}</h2>

          <p className="mt-1 text-slate-500">{type}</p>

          <div className="mt-4 flex gap-6 text-sm text-slate-600">
            <span>Features: {features}</span>
            <span>Observations: {observations}</span>
          </div>
        </div>

        <Button onClick={onOpen}>Open</Button>
      </div>
    </Card>
  );
}

export default CategoryCard;
