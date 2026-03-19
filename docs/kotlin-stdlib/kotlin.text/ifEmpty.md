

# ifEmpty

Returns this char sequence if it's not empty or the result of calling defaultValue function if the char sequence is empty.

```kotlin
inline fun <C : CharSequence, R, R> C.ifEmpty(defaultValue: () -> R): R(source)
```

```kotlin
fun main() {
    val nonEmpty = "Kotlin".ifEmpty { "Default" }
    val empty = "".ifEmpty { "Default" }

    println(nonEmpty) // Kotlin
    println(empty)    // Default
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/if-empty.html)

    