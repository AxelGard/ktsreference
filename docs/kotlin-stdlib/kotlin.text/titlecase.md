

# titlecase

Converts this character to title case using Unicode mapping rules of the invariant locale.

```kotlin
fun Char.titlecase(): String(source)
```

```kotlin
fun main() {
    val char: Char = 'k'
    val titleCase = char.titlecase()
    println(titleCase)  // prints: "K"
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/titlecase.html)

    