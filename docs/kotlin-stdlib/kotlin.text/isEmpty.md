

# isEmpty

Returns true if this char sequence is empty (contains no characters).

```kotlin
inline fun CharSequence.isEmpty(): Boolean(source)
```

```kotlin
fun main() {
    val emptyString: CharSequence = ""
    val nonEmptyString: CharSequence = "Hello, Kotlin!"

    println("emptyString.isEmpty() = ${emptyString.isEmpty()}")      // true
    println("nonEmptyString.isEmpty() = ${nonEmptyString.isEmpty()}") // false
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/is-empty.html)

    