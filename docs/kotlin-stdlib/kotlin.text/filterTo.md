

# filterTo

Appends all characters matching the given predicate to the given destination.

```kotlin
@IgnorableReturnValueinline fun <C : Appendable> CharSequence.filterTo(destination: C, predicate: (Char) -> Boolean): C(source)
```

```kotlin
fun main() {
    val source = "a1b2c3"
    val result = StringBuilder()
    source.filterTo(result) { it.isDigit() }
    println(result.toString()) // prints 123
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.text/filter-to.html)

    