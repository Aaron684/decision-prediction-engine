import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

import {
  getCategories,
  deleteCategory,
  type Category,
} from "../api/Categories";

import PageLayout from "../components/layout/PageLayout";
import PageHeader from "../components/layout/PageHeader";

import CategoryCard from "../components/categories/CategoryCard";
import CategoryForm from "../components/categories/CategoryForm";

import Card from "../components/ui/Card";
import ConfirmDialog from "../components/ui/ConfirmDialogue";

import { useToast } from "../context/ToastContext";

function Categories() {
  const navigate = useNavigate();
  const toast = useToast();

  const [categories, setCategories] = useState<Category[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  const [editingCategory, setEditingCategory] = useState<
    Category | undefined
  >();

  const [deletingCategory, setDeletingCategory] = useState<
    Category | undefined
  >();

  async function loadCategories() {
    try {
      setLoading(true);

      const result = await getCategories();

      setCategories(result);
      setError(null);
    } catch {
      setError("Unable to load categories.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadCategories();
  }, []);

  async function handleDelete() {
    if (!deletingCategory) {
      return;
    }

    try {
      await deleteCategory(deletingCategory.id);

      toast.success("Category deleted.");

      setDeletingCategory(undefined);

      await loadCategories();
    } catch {
      toast.error("Unable to delete category.");
    }
  }

  if (loading) {
    return (
      <PageLayout>
        <PageHeader title="Categories" subtitle="Loading categories..." />
      </PageLayout>
    );
  }

  if (error) {
    return (
      <PageLayout>
        <PageHeader title="Categories" subtitle="Something went wrong." />

        <Card>
          <p className="text-red-600">{error}</p>
        </Card>
      </PageLayout>
    );
  }

  return (
    <PageLayout>
      <PageHeader
        title="Categories"
        subtitle="Create and manage prediction problems."
      />

      <div className="mt-8">
        <CategoryForm
          category={editingCategory}
          onSaved={async () => {
            setEditingCategory(undefined);
            await loadCategories();
          }}
          onCancel={() => setEditingCategory(undefined)}
        />
      </div>

      <div className="mt-8 space-y-6">
        {categories.length === 0 ? (
          <Card>
            <p className="text-slate-500">
              No categories have been created yet.
            </p>
          </Card>
        ) : (
          categories.map((category) => (
            <CategoryCard
              key={category.id}
              id={category.id}
              name={category.name}
              type={
                category.target_type.charAt(0).toUpperCase() +
                category.target_type.slice(1)
              }
              description={category.description}
              target={category.target_name}
              features={0}
              observations={0}
              onOpen={() => navigate(`/categories/${category.id}`)}
              onEdit={() => {
                setEditingCategory(category);

                window.scrollTo({
                  top: 0,
                  behavior: "smooth",
                });
              }}
              onDelete={() => {
                setDeletingCategory(category);
              }}
            />
          ))
        )}
      </div>

      <ConfirmDialog
        open={deletingCategory !== undefined}
        title="Delete Category"
        message={
          deletingCategory
            ? `Delete "${deletingCategory.name}"? This will also remove all features and observations.`
            : ""
        }
        confirmText="Delete"
        onConfirm={handleDelete}
        onCancel={() => setDeletingCategory(undefined)}
      />
    </PageLayout>
  );
}

export default Categories;
