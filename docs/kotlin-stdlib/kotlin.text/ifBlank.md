

# ifBlank

Returns this char sequence if it is not empty and doesn't consist solely of whitespace characters, or the result of calling defaultValue function otherwise.

```kotlin
inline fun <C : CharSequence, R, R> C.ifBlank(defaultValue: () -> R): R(source)
```

```kotlin
fun main() {
    val empty = "   "
    println(empty.ifBlank { "Default value" })   // prints: Default value

    val nonEmpty = "Hello"
    println(nonEmpty.ifBlank { "Default value" }) // prints: Hello
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/if-blank.html)

    