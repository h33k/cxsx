import supernotes as sn
import md
import json
import os
import customization as cus

if __name__ == '__main__':
    cards = sn.cards.getCards(os.environ.get('API_KEY'))
    cards = json.loads(cards)

    for card_id, card in cards.items():
        markup = card['data']['markup']
        title = card['data']['name']
        created_when, *_ = card['data']['created_when'].replace('T', '-').replace(':', '-').partition('.')
        modified_when = card['data']['modified_when']
        tags = card['data']['tags']
        author = 'superpages'

        args = dict(title=title,date=created_when, tags=tags, author=author, modified_when=modified_when)
        md_filename = created_when

        if cus.isCustomizationCard(tags):
            cus.updateCustomization(title, markup, modified_when)
            break

        if md.mdf.is_modified(md_filename, modified_when):
            md.mdf.delete_md_with_date_prefix(md_filename)
            md.mdw.write_frontmatter(args)
            md.mdw.write_body(args, markup)
