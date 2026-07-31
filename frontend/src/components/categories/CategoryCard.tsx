import { Pencil, Trash2 } from "lucide-react";

import Button from "../ui/Button";
import Card from "../ui/Card";
import IconButton from "../ui/IconButton";

interface CategoryCardProps {
  id: number;

  name: string;

  type: string;

  description: string;

  target: string;

  features: number;

  observations: number;

  onOpen?: () => void;

  onEdit: () => void;

  onDelete: () => void;
}

function CategoryCard({
  name,
  type,
  description,
  target,
  features,
  observations,
  onOpen,
  onEdit,
  onDelete,
}: CategoryCardProps) {
  return (
    <Card>
      <div className="flex justify-between">
        <div>
          <h2 className="text-xl font-semibold text-slate-800">{name}</h2>

          <p className="text-slate-500">{type}</p>

          <p className="mt-3 text-slate-600">{description}</p>

          <p className="mt-2 text-sm text-slate-500">Target: {target}</p>

          <div className="mt-4 flex gap-6 text-sm">
            <span>Features: {features}</span>

            <span>Observations: {observations}</span>
          </div>
        </div>

        <div className="flex gap-2">
          <Button onClick={onOpen}>Open</Button>

          <IconButton title="Edit" onClick={onEdit}>
            <Pencil size={18} />
          </IconButton>

          <IconButton title="Delete" onClick={onDelete}>
            <Trash2 size={18} />
          </IconButton>
        </div>
      </div>
    </Card>
  );
}

export default CategoryCard;
