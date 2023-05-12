import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file


essay = f"""
Biodiversity is really important for maintain ecosystem balance. The world is home to a wide variety of living things, such as plants, animals, and microbes. This variety is known as biodiversity. However, humans are destroying many habitats and causing many species to become extinct. This is not good for the environment, and it can cause many problems for humans as well.
One important reason why biodiversity is important is because it helps to keep the balance of the ecosystem. Different living things rely on each other to survive, and if one species disappears, it can cause a chain reaction that affects many other species. For example, if bees become extinct, it would be really bad for plants, because bees are important pollinators. Without bees, many plants would not be able to reproduce, and this could cause problems for humans who rely on these plants for food.
Another reason why biodiversity is important is because it provides many benefits to humans. For example, many medicines come from plants and animals, and we rely on many crops that are pollinated by bees and other insects. Also, nature is really beautiful, and many people enjoy spending time outdoors, such as hiking or camping.
However, there are many problems that are threatening biodiversity. For example, deforestation, climate change, and pollution are causing many habitats to disappear, which is causing many species to become extinct. This is really bad for the environment, and it can cause many problems for humans as well.
In conclusion, biodiversity is really important for maintain ecosystem balance. It is threatened by many problems, but we can do things to protect it, such as reducing our carbon footprint, using fewer pesticides, and preserving natural habitats. We all have a responsibility to take care of our planet and preserve the biodiversity that makes life possible.
"""

grammar = f"""
So + adjective + that Clause; 2. In spite of + noun/gerund/doing something; 3. Despite + noun/gerund/doing something; 4. Not only + Verb (but) also + Verb; 5. While + subject + verb, subject + verb; 6. The + comparative + Clause, the + comparative + Clause; 7. It is + adjective + that + subject + verb; 8. Although/Even though + subject + verb, subject + verb; 9. Due to + noun/gerund/doing something; 10. Thanks to + noun/gerund/doing something; 11. Such + noun + that + Clause; 12. As + subject + verb, subject + verb; 13. If + subject + verb, subject + will/would + verb; 14. Because of + noun/gerund/doing something; 15. One + verb + noun, another + verb + noun; 16. In order to + verb, subject + verb; 17. As a result of + noun/gerund/doing something; 18. On the one hand + Clause, on the other hand + Clause; 19. Without + noun/gerund/doing something, subject + cannot/could not + verb; 20. To be + adjective + to + verb; 21. No sooner + did + subject + verb, than + subject + verb; 22. Just as + subject + verb, subject + verb; 23. Both + noun + and + noun; 24. Neither + noun + nor + noun; 25. Either + noun + or + noun; 26. The more + adjective + Clause, the more + adjective + Clause; 27. The less + adjective + Clause, the less + adjective + Clause; 28. More + adjective + than + noun; 29. Less + adjective + than + noun; 30. More + noun + than + noun; 31. Less + noun + than + noun; 32. Verb + the + noun + out of + noun; 33. Verb + noun + to + verb; 34. The more + noun + Clause, the more + noun + Clause; 35. The less + noun + Clause, the less + noun + Clause; 36. Whether + Clause or not; 37. Not only + noun + but also + noun; 38. Sooner or later + subject + will + verb; 39. All + noun + need to do is + verb; 40. Little + noun + that + subject + verb; 41. No + noun + that + subject + verb; 42. As if + subject + verb; 43. As though + subject + verb; 44. In case + subject + verb; 45. Just in case + subject + verb; 46. Rather than + verb, subject + will/would + verb; 47. On condition that + subject + verb; 48. So as to + verb; 49. Such + adjective + noun + that + Clause; 50. Just like + noun + noun; 51. Not until + subject + verb, did + subject + verb; 52. All things considered + Clause; 53. At first + subject + verb, but later + subject + verb; 54. Be that as it may + Clause; 55. Even if/though + subject + verb, subject + verb
"""

vocabulary = f"""
Abiotic, Ablation, Acclimation, Adaptation, Aerobic, Agar, Allele, Allopatric, Allosteric, Amoeba, Amphibian, Anaerobic, Anatomy, Angiosperm, Antibody, Antigen, Aorta, Apoptosis, Artery, Asexual, Autosome, Bacteria, Bacteriophage, Basal, Benthic, Biennial, Biochemistry, Biodiversity, Biogeography, Bioluminescence, Biomass, Biome, Biopsy, Biosphere, Biotechnology, Biotic, Blastocyst, Blood, Bone, Botany, Brain, Cambium, Capillary, Carbohydrate, Carnivore, Carotenoid, Cartilage, Catabolism, Cell, Cellulose, Centriole, Cerebellum, Cerebral, Cervix, Chlorophyll, Chloroplast, Chromosome, Cilia, Cladogram, Climate, Clone, Codon, Community, Competition, Conifer, Connective tissue, Conservation, Consumer, Cytokinesis, Cytology, Cytoskeleton, Darwinism, Deciduous, Decomposer, Deoxyribonucleic acid (DNA), Desert, Development, Diaphragm, Digestion, Dihybrid, Diploid, DNA fingerprinting, Dominance, Ecosystem, Ectoderm, Ectothermic, Edaphic, Egg, Electrophoresis, Embryo, Endemic, Endocrine, Endocytosis, Endoderm, Endoplasmic reticulum, Endosperm, Energy, Enzyme, Epidermis, Epithelial tissue, Erythrocyte, Estuary, Evolution, Excretion, Exoskeleton, Exotic, Extinct, Fatty acid, Fermentation, Fertilization, Fiber, Fish, Flagella, Flora, Flower, Fossil, Frond, Fungi, Gamete, Gametogenesis, Gametophyte, Gene, Gene expression, Genotype, Germ cells, Germ layers, Germ plasm, Giantism, Gibberellin, Gills, Glucose, Glycogen, Golgi apparatus, Gonad, Gymnosperm, Habitat, Haploid, Hemoglobin, Herbivore, Heterotroph, Hibernation, Histology, Homeostasis, Homologous, Hormone, Host, Hybrid, Hydroponics, Hypertonic, Hypotonic, Immune system, Inbreeding, Insect, Insectivore, Invasive, Ion, Isotope, Keratin, Kingdom, Kinetochore, Karyotype, Larva, Lateral line, Lenticels, Leukocyte, Ligament, Lipid, Locus, Lysosome, Macroevolution, Macronutrient, Meiosis, Metabolism, Metaphase, Microbe, Microevolution, Microorganism, Mitochondrion, Mitosis, Monocot, Mutation, Mycorrhiza, Natural selection, Nervous system, Nitrogen cycle, Nucleic acid, Nucleotide, Nutrient, Oocyte, Oogenesis, Osmosis, Ovary, Oviduct, Parasite, Parenchyma, Pathogen, Pedigree, Peptide, Photosynthesis
"""

prompt = f"""
You are a expert english teacher.
Your task is to give me suggestion  how to improve grammar, vocabulary, context for the essay
Given the student essay delimited by ```, \
Given the  grammar delimited by ```, \
Given the vocabulary delimited by ```, \
Write in a concise and professional tone.
Can you give me suggestion  how to improve grammar, vocabulary, context for the student essay based on vocabulary , grammar  ? 
Student essay: ```{essay}```
Vocabulary: ```{vocabulary}```
Grammar: ```{grammar}```
"""

openai.api_key  = "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"

def get_completion(prompt, model="davinci:ft-personal-2023-05-08-14-12-48",temperature=0): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.Completion.create(
        model=model,
        prompt=prompt
        # this is the degree of randomness of the model's output
    )
    return response

prompt = f"""this is an example and not the real json ->"""
response = get_completion(prompt)
print(response)