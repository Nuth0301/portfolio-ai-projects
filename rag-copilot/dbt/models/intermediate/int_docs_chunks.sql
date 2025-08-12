-- Example: create chunked text (replace with real logic)
with src as (
  select doc_id, text_content from {{ source('raw', 'docs_text') }}
)
select 
  doc_id,
  substr(text_content, 1, 800) as chunk_text,
  1 as chunk_id
from src
