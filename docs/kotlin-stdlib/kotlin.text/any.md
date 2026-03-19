

# any

Returns true if char sequence has at least one character.

```kotlin
fun CharSequence.any(): Boolean(source)
```

```kotlin
fun main() {
    val nonEmpty = "Kotlin".any()   // true, because there is at least one character
    val empty = "".any()            // false, because the sequence has no characters

    println("Non‑empty: $nonEmpty") // prints: Non‑empty: true
    println("Empty: $empty")        // prints: Empty: false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/any.html)

    