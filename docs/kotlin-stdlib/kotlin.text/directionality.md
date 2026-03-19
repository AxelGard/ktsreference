

# directionality

Returns the Unicode directionality property for the given character.

```kotlin
val Char.directionality: CharDirectionality(source)
```

```kotlin
import kotlin.text.*

fun main() {
    val sample = "אבג123"
    for (ch in sample) {
        println("Character: '$ch' → Directionality: ${ch.directionality}")
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/directionality.html)

    