-- Example mart: join chunks to embeddings (placeholder)
select 
  c.doc_id, 
  c.chunk_id,
  c.chunk_text,
  e.embedding -- VARIANT or VECTOR
from {{ ref('int_docs_chunks') }} c
left join {{ ref('feat_doc_embeddings') }} e
  on c.doc_id = e.doc_id and c.chunk_id = e.chunk_id
