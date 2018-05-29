from django.shortcuts import render
from .models import Collection
from django.conf import settings
from elasticsearch_dsl import Search
from elasticsearch_dsl.connections import connections

def community_detail(request, community_name):
    """Community detail page"""
    client = connections.get_connection()

    context = {} # Context data

    def community_detail(community_name):
        """
        Function to return the list of collection name and total item from this collection.
        """
        # Get all the collections from community.
        collection_list = []
        all_total = 0
        collections = Collection.objects.filter(community_name=community_name)
        
        for collection in collections:
            item_count_per_collection = Search(index="pustakalaya").using(client).query("match",collections_ids=collection.pk).count()
            all_total += item_count_per_collection
            pk = collection.pk

            # Create a list to that contain collection_name and total count
            collection_list.append({
            "collection_name": collection.collection_name,
            "total_count": all_total,
            "es_count": item_count_per_collection,
            "pk": pk,
            })  

        return {
            "community_name": community_name,
            "collection_list": collection_list
        }
  
    # Query literature and arts detail 
    literature_and_arts = list(map(community_detail, ['literatures and arts']))[0]
    context["literature_and_arts"] = literature_and_arts

    # Query course materials 
    course_materials = list(map(community_detail, ['course materials']))[0]
    context["course_materials"] = course_materials

    # Query teaching materials
    teaching_materials = list(map(community_detail, ['teaching materials']))[0]
    context["teaching_materials"] = teaching_materials

    # Query reference materials detail 
    reference_materials = list(map(community_detail, ['reference materials']))[0]
    context["reference_materials"] = reference_materials

    # Query newpapers and magazines detail 
    newpapers_and_magazines = list(map(community_detail, ['newpapers and magazines']))[0]
    context["newpapers_and_magazines"] = newpapers_and_magazines
    
    # Query newpapers and magazines detail 
    othereducational_materials = list(map(community_detail, ['othereducational materials']))[0]
    context["othereducational_materials"] = othereducational_materials

    return render(request, "collection/community_detail.html", context)
