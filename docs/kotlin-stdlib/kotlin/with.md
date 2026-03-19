

# with

Calls the specified function block with the given receiver as its receiver and returns its result.

```kotlin
@IgnorableReturnValueinline fun <T, R> with(receiver: T, block: T.() -> R): R(source)
```

```kotlin
// Using `with` to build a string
val greeting = with(StringBuilder()) {
    append("Hello, ")
    append("world!")
    toString()
}
println(greeting)   // prints: Hello, world!
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/with.html)

    