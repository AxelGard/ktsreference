

# none

Returns true if the char sequence has no characters.

```kotlin
fun CharSequence.none(): Boolean(source)
```

```kotlin
fun main() {
    val nonEmpty = "Kotlin"
    val empty = ""

    println("nonEmpty.none() = ${nonEmpty.none()}") // prints: false
    println("empty.none() = ${empty.none()}")       // prints: true
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/none.html)

    