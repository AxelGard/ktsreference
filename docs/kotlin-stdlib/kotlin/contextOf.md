

# contextOf

Retrieves the context argument, extension or dispatch receiver in scope with the given type. The compiler ensures that at least one such given value exists. If more than one is found, more nested scopes are prioritized, and otherwise an ambiguity error is raised by the compiler.

```kotlin
context(context: A)inline fun <A> contextOf(): A(source)
```

```kotlin
class MyContext(val name: String)

fun <T> withContext(context: T, block: T.() -> Unit) = context.block()

fun main() {
    val ctx = MyContext("Example")
    withContext(ctx) {
        // Inside this lambda, `MyContext` is the contextual receiver.
        val c = contextOf<MyContext>()   // retrieves the contextual receiver
        println(c.name)                  // prints: Example
    }
}
```

[Source](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/context-of.html)

    