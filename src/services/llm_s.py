import os
import random
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.callbacks import get_openai_callback
def random_key_openai():
    list_key = [
        "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",
        "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",
        "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",
        "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",
    ]
    OPEN_API_KEY = random.choice(list_key)
    print("OPEN_API_KEY :" +OPEN_API_KEY)
    os.environ["OPENAI_API_KEY"]=OPEN_API_KEY
random_key_openai()

def suggestion(essay,topic,level,vol,gram):
    random_key_openai()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo")
    template = """
    Can you give me suggestion how to improve {essay} for biology topic based on  ielts 7.0 \nGramary : So + adjective + that Clause; 2. In spite of + noun/gerund/doing something; 3. Despite + noun/gerund/doing something; 4. Not only + Verb (but) also + Verb; 5. While + subject + verb, subject + verb; 6. The + comparative + Clause, the + comparative + Clause; 7. It is + adjective + that + subject + verb; 8. Although/Even though + subject + verb, subject + verb; 9. Due to + noun/gerund/doing something; 10. Thanks to + noun/gerund/doing something; 11. Such + noun + that + Clause; 12. As + subject + verb, subject + verb; 13. If + subject + verb, subject + will/would + verb; 14. Because of + noun/gerund/doing something; 15. One + verb + noun, another + verb + noun; 16. In order to + verb, subject + verb; 17. As a result of + noun/gerund/doing something; 18. On the one hand + Clause, on the other hand + Clause; 19. Without + noun/gerund/doing something, subject + cannot/could not + verb; 20. To be + adjective + to + verb; 21. No sooner + did + subject + verb, than + subject + verb; 22. Just as + subject + verb, subject + verb; 23. Both + noun + and + noun; 24. Neither + noun + nor + noun; 25. Either + noun + or + noun; 26. The more + adjective + Clause, the more + adjective + Clause; 27. The less + adjective + Clause, the less + adjective + Clause; 28. More + adjective + than + noun; 29. Less + adjective + than + noun; 30. More + noun + than + noun; 31. Less + noun + than + noun; 32. Verb + the + noun + out of + noun; 33. Verb + noun + to + verb; 34. The more + noun + Clause, the more + noun + Clause; 35. The less + noun + Clause, the less + noun + Clause; 36. Whether + Clause or not; 37. Not only + noun + but also + noun; 38. Sooner or later + subject + will + verb; 39. All + noun + need to do is + verb; 40. Little + noun + that + subject + verb; 41. No + noun + that + subject + verb; 42. As if + subject + verb; 43. As though + subject + verb; 44. In case + subject + verb; 45. Just in case + subject + verb; 46. Rather than + verb, subject + will/would + verb; 47. On condition that + subject + verb; 48. So as to + verb; 49. Such + adjective + noun + that + Clause; 50. Just like + noun + noun; 51. Not until + subject + verb, did + subject + verb; 52. All things considered + Clause; 53. At first + subject + verb, but later + subject + verb; 54. Be that as it may + Clause; 55. Even if/though + subject + verb, subject + verb
    \nVocabulary: Abiotic, Ablation, Acclimation, Adaptation, Aerobic, Agar, Allele, Allopatric, Allosteric, Amoeba, Amphibian, Anaerobic, Anatomy, Angiosperm, Antibody, Antigen, Aorta, Apoptosis, Artery, Asexual, Autosome, Bacteria, Bacteriophage, Basal, Benthic, Biennial, Biochemistry, Biodiversity, Biogeography, Bioluminescence, Biomass, Biome, Biopsy, Biosphere, Biotechnology, Biotic, Blastocyst, Blood, Bone, Botany, Brain, Cambium, Capillary, Carbohydrate, Carnivore, Carotenoid, Cartilage, Catabolism, Cell, Cellulose, Centriole, Cerebellum, Cerebral, Cervix, Chlorophyll, Chloroplast, Chromosome, Cilia, Cladogram, Climate, Clone, Codon, Community, Competition, Conifer, Connective tissue, Conservation, Consumer, Cytokinesis, Cytology, Cytoskeleton, Darwinism, Deciduous, Decomposer, Deoxyribonucleic acid (DNA), Desert, Development, Diaphragm, Digestion, Dihybrid, Diploid, DNA fingerprinting, Dominance, Ecosystem, Ectoderm, Ectothermic, Edaphic, Egg, Electrophoresis, Embryo, Endemic, Endocrine, Endocytosis, Endoderm, Endoplasmic reticulum, Endosperm, Energy, Enzyme, Epidermis, Epithelial tissue, Erythrocyte, Estuary, Evolution, Excretion, Exoskeleton, Exotic, Extinct, Fatty acid, Fermentation, Fertilization, Fiber, Fish, Flagella, Flora, Flower, Fossil, Frond, Fungi, Gamete, Gametogenesis, Gametophyte, Gene, Gene expression, Genotype, Germ cells, Germ layers, Germ plasm, Giantism, Gibberellin, Gills, Glucose, Glycogen, Golgi apparatus, Gonad, Gymnosperm, Habitat, Haploid, Hemoglobin, Herbivore, Heterotroph, Hibernation, Histology, Homeostasis, Homologous, Hormone, Host, Hybrid, Hydroponics, Hypertonic, Hypotonic, Immune system, Inbreeding, Insect, Insectivore, Invasive, Ion, Isotope, Keratin, Kingdom, Kinetochore, Karyotype, Larva, Lateral line, Lenticels, Leukocyte, Ligament, Lipid, Locus, Lysosome, Macroevolution, Macronutrient, Meiosis, Metabolism, Metaphase, Microbe, Microevolution, Microorganism, Mitochondrion, Mitosis, Monocot, Mutation, Mycorrhiza, Natural selection, Nervous system, Nitrogen cycle, Nucleic acid, Nucleotide, Nutrient, Oocyte, Oogenesis, Osmosis, Ovary, Oviduct, Parasite, Parenchyma, Pathogen, Pedigree, Peptide, Photosynthesis ?
    """
    prompt = PromptTemplate(
        input_variables=["essay"],
        template=template
    )
    chain = LLMChain(llm=llm, prompt=prompt,verbose=True)
    # with get_openai_callback() as cb:
    #     response = chain.predict(essay=essay)
    res = chain.run({"essay":essay})
    res = chain.run({"essay":essay})
    return res
    